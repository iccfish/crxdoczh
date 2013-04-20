# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import logging
import os
from StringIO import StringIO
import json

from appengine_wrappers import webapp
from appengine_wrappers import memcache
from appengine_wrappers import urlfetch
from branch_utility import BranchUtility
from server_instance import ServerInstance
import svn_constants
import time
from response_cache import ResponseCache

# The default channel to serve docs for if no channel is specified.
_DEFAULT_CHANNEL = 'stable'

class Handler(webapp.RequestHandler):
  # AppEngine instances should never need to call out to SVN. That should only
  # ever be done by the cronjobs, which then write the result into DataStore,
  # which is as far as instances look.
  #
  # Why? SVN is slow and a bit flaky. Cronjobs failing is annoying but
  # temporary. Instances failing affects users, and is really bad.
  #
  # Anyway - to enforce this, we actually don't give instances access to SVN.
  # If anything is missing from datastore, it'll be a 404. If the cronjobs
  # don't manage to catch everything - uhoh. On the other hand, we'll figure it
  # out pretty soon, and it also means that legitimate 404s are caught before a
  # round trip to SVN.
  #
  # However, we can't expect users of preview.py to run a cronjob first, so,
  # this is a hack allow that to be online all of the time.
  # TODO(kalman): achieve this via proper dependency injection.
  ALWAYS_ONLINE = True

  def __init__(self, request, response):
    super(Handler, self).__init__(request, response)

  def _OriginalHandleGet(self, path):
    channel_name, real_path = BranchUtility.SplitChannelNameFromPath(path)

    if channel_name == _DEFAULT_CHANNEL:
      self.redirect('/%s' % real_path)
      return

    if channel_name is None:
      channel_name = _DEFAULT_CHANNEL

    # TODO(kalman): Check if |path| is a directory and serve path/index.html
    # rather than special-casing apps/extensions.
    if real_path.strip('/') == 'apps':
      real_path = 'apps/index.html'
    if real_path.strip('/') == 'extensions':
      real_path = 'extensions/index.html'

    constructor = (
        ServerInstance.GetOrCreateOnline if Handler.ALWAYS_ONLINE else
        ServerInstance.GetOrCreateOffline)
    server_instance = constructor(channel_name)

    canonical_path = server_instance.path_canonicalizer.Canonicalize(real_path)
    if real_path != canonical_path:
      self.redirect(canonical_path)
      return

    server_instance.Get(real_path, self.request, self.response)

  def _HandleGet(self, path):
    if os.environ.get('CRXDOCZH_SLAVE_TYPE') is None:
      self._OriginalHandleGet(path)
      return

    channel_name, real_path = BranchUtility.SplitChannelNameFromPath(path)
    if channel_name is None:
      channel_name = _DEFAULT_CHANNEL

    if os.environ.get('CRXDOCZH_SLAVE_TYPE') == 'samples':
      self._HandleSamplesAPI(channel_name, real_path)
    else:
      server_instance = ServerInstance.GetOrCreate(channel_name)

      canonical_path = server_instance.path_canonicalizer.Canonicalize(real_path)
      if real_path != canonical_path:
        self.redirect(canonical_path)
        return

      ServerInstance.GetOrCreate(channel_name).Get(real_path,
                                                   self.request,
                                                   self.response)

  def _HandleBackends(self):
    self.response.set_status(200)
    self.response.write('Started')
    if os.environ.get('CRXDOCZH_SLAVE_TYPE') == 'samples':
      self._HandleSamplesBackends()
    elif os.environ.get('CRXDOCZH_SLAVE_TYPE') == 'docs':
      self._HandleDocsBackends()
    self.response.write('Completed')

  def _HandleSamplesAPI(self, channel_name, real_path):
    if real_path.startswith(url_constants.SLAVE_SAMPLES_API_BASE_URL):
      key = real_path[len(url_constants.SLAVE_SAMPLES_API_BASE_URL):]
      if key == 'apps' or key == 'extensions':
        self.response.headers['content-type'] = 'text/plain'
        cache_url = None
        if key == 'apps':
          cache_url = '/trunk/' + key
        else:
          cache_url = '/' + channel_name + '/' + key
        logging.info('Serving API request %s' % cache_url)
        data = ResponseCache.Get(cache_url)
        if data is None:
          self.response.out.write('[]')
          logging.error('No samples data. Please regenerate it manually.')
        else:
          self.response.out.write(data)
      else:
        self.response.set_status(404)
    else:
      self.response.set_status(404)

  def _HandleSamplesBackends(self):
    for channel in ['trunk', 'dev', 'beta', 'stable']:
      self._CacheSamplesJSON(channel, 'extensions', update=True)
      import time
      time.sleep(5)

    self._CacheSamplesJSON('trunk', 'apps', update=True)

  def _HandleFeedUpdate(self):
    from subversion_file_system import StatUpdater
    StatUpdater.Update()
    self.response.status = 200

  def _CacheSamplesJSON(self, channel, key, update=False):
    class MockRequest(object):
      def __init__(self, path):
        self.headers = {}
        self.path = path
        self.url = '//localhost/%s' % path

    count = 0
    while count < 10:
      constructor = (
          ServerInstance.GetOrCreateOnline if Handler.ALWAYS_ONLINE else
          ServerInstance.GetOrCreateOffline)
      server_instance = constructor(channel)
      result = server_instance._GetSamplesJSON(
          MockRequest('/' + channel + '/' + key + '/samples.html'),
          key, update)
      if(len(result) > 0):
        return
      count += 1
      import time
      time.sleep(5 * count)

  def _HandleDocsBackends(self):
    return

  def _HandleCron(self, path):
    # Cron strategy:
    #
    # Find all public template files and static files, and render them. Most of
    # the time these won't have changed since the last cron run, so it's a
    # little wasteful, but hopefully rendering is really fast (if it isn't we
    # have a problem).
    class MockResponse(object):
      def __init__(self):
        self.status = 200
        self.out = StringIO()
        self.headers = {}
      def set_status(self, status):
        self.status = status
      def clear(self, *args):
        pass

    class MockRequest(object):
      def __init__(self, path):
        self.headers = {}
        self.path = path
        self.url = '//localhost/%s' % path

    channel = path.split('/')[-1]
    logging.info('cron/%s: starting' % channel)

    server_instance = ServerInstance.GetOrCreateOnline(channel)

    def run_cron_for_dir(d, path_prefix=''):
      success = True
      start_time = time.time()
      files = [f for f in server_instance.content_cache.GetFromFileListing(d)
               if not f.endswith('/')]
      for f in files:
        error = None
        path = '%s%s' % (path_prefix, f)
        try:
          response = MockResponse()
          server_instance.Get(path, MockRequest(path), response)
          if response.status != 200:
            error = 'Got %s response' % response.status
          try:
            urlfetch.fetch(url_constants.CRXDOCZH_MASTER_UPDATE_URL,
                payload = json.dumps([f]),
                method = 'POST',
                deadline = 6)
          except Exception as e:
            pass
          try:
            urlfetch.fetch(url_constants.CRXDOCZH_MASTER_MIRROR_UPDATE_URL,
                payload = json.dumps([f]),
                method = 'POST',
                deadline = 6)
          except Exception as e:
            pass
        except error:
          pass
        if error:
          logging.error('cron/%s: error rendering %s: %s' % (
              channel, path, error))
          success = False
      logging.info('cron/%s: rendering %s files took %s seconds' % (
          channel, len(files), time.time() - start_time))
      return success

    # Don't use "or" since we want to evaluate everything no matter what.
    success = any((
        # Note: rendering the public templates will pull in all of the private
        # templates.
        run_cron_for_dir(svn_constants.PUBLIC_TEMPLATE_PATH),
        run_cron_for_dir(svn_constants.STATIC_PATH, path_prefix='static/'),
        # Note: rendering the public templates will have pulled in the .js and
        # manifest.json files (for listing examples on the API reference pages),
        # but there are still images, CSS, etc.
        # run_cron_for_dir(svn_constants.EXAMPLES_PATH,
        #                 path_prefix='extensions/examples/')
                 ))

    if success:
      self.response.status = 200
      self.response.out.write('Success')
    else:
      self.response.status = 500
      self.response.out.write('Failure')

    logging.info('cron/%s: finished' % channel)

  def _RedirectSpecialCases(self, path):
    google_dev_url = 'http://developer.google.com/chrome'
    if path == '/' or path == '/index.html':
      self.redirect(google_dev_url)
      return True

    if path == '/apps.html':
      self.redirect('/apps/about_apps.html')
      return True

    return False

  def _RedirectFromCodeDotGoogleDotCom(self, path):
    if (not self.request.url.startswith(('http://code.google.com',
                                         'https://code.google.com'))):
      return False

    new_url = 'http://developer.chrome.com/'

    # switch to https if necessary
    if (self.request.url.startswith('https')):
      new_url = new_url.replace('http', 'https', 1)

    path = path.split('/')
    if len(path) > 0 and path[0] == 'chrome':
      path.pop(0)
    for channel in BranchUtility.GetAllBranchNames():
      if channel in path:
        position = path.index(channel)
        path.pop(position)
        path.insert(0, channel)
    new_url += '/'.join(path)
    self.redirect(new_url)
    return True

  def _OriginalGet(self):
    path = self.request.path

    if path in ['favicon.ico', 'robots.txt']:
      response.set_status(404)
      return

    if self._RedirectSpecialCases(path):
      return

    if path.startswith('/cron'):
      self._HandleCron(path)
      return

    # Redirect paths like "directory" to "directory/". This is so relative
    # file paths will know to treat this as a directory.
    if os.path.splitext(path)[1] == '' and path[-1] != '/':
      self.redirect(path + '/')
      return

    path = path.strip('/')
    if self._RedirectFromCodeDotGoogleDotCom(path):
      return

    self._HandleGet(path)

  def get(self):
    if os.environ.get('CRXDOCZH_SLAVE_TYPE') is None:
      self._OriginalGet()
      return

    path = self.request.path
    if path.startswith('/_ah/start'):
      self._HandleBackends()
    elif path == '/_/update':
      self._HandleFeedUpdate()
    elif path.startswith('/cron'):
      self._HandleCron(path)
      return
    else:
      self._HandleGet(path.strip('/'))
