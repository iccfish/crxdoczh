import json, logging, mimetypes, os, webapp2
from google.appengine.api import urlfetch, memcache
from google.appengine.ext import db
from redirects import REDIRECTS

class CacheModel(db.Expando):
  data = db.BlobProperty(required=True)

class Cache:
  @staticmethod
  def get(path):
    if path is None:
      return None

    path = '/stable' + path
    data = memcache.get(path)
    if data is not None:
      return data

    model = db.get(db.Key.from_path('CacheModel', path))
    if model is not None:
      memcache.add(path, model.data)
      return model.data

    return None

  @staticmethod
  def update(path, data):
    components = path.strip('/').split('/')
    model = CacheModel(key_name = path,
                       data = data,
                       **{'path[%s]' % i: components[i]
                        for i in range(len(components))})
    model.put()
    if memcache.get(path) is not None:
      memcache.set(path, data)

def _AddSecurityHeaders(response):
  return
  response.headers.add('Strict-Transport-Security',
                       'max-age=31536000')
  # Keep these synced with https://src.chromium.org/viewvc/chrome/trunk/src/net/base/transport_security_state_static.certs
  response.headers.add('Public-Key-Pins',
                       'max-age=2592000; ' + 
                       'pin-sha1="4n972HfV354KP560yw4uqe/baXc="; ' +
                       'pin-sha1="IvGeLsbqzPxdI0b0wuj2xVTdXgc="; ' +
                       'pin-sha1="QMVAHW+MuvCLAO3vse6H0AWzuc0="; ' +
                       'pin-sha1="AbkhxY0L343gKf+cki7NVWp+ozk="; ' +
                       'pin-sha1="fVujyo43ZR18ccPjt3TN6XsbWUM="; ' +
                       'pin-sha1="vq7OyjSnqOco9nyMCDGdy77eijM="; ' +
                       'pin-sha1="SOZo+SvSspXXR9gjIBBPM5iQn9Q="; ' +
                       'pin-sha1="wHqYaI2J+6sFZAwRfap9ZbjKzE4="')
  response.headers.add('X-Frame-Options', 'SAMEORIGIN')

def _AddCanonicalLinkHeader(normalized_path, response):
  response.headers.add('Link',
      '<https://crxdoc-zh.appspot.com%s>; rel="canonical"' % normalized_path)

# Parameters:
# |doc_type|: apps|extensions|static
# |remaining_path|: xxx.html|css/xxx.css|...
# Returns:
# A path that can be passed to Cache or None if invalid.
def NormalizePath(doc_type, remaining_path):
  path = '/'
  path2 = None
  if doc_type is not None:
    if doc_type == 'extensions':
      path2 = path + 'apps/'
    elif doc_type == 'apps':
      path2 = path + 'extensions/'
    path += doc_type + '/'

  if doc_type == 'static':
    return (path + remaining_path, None, False)
  else:
    if not remaining_path.endswith('.html'):
      return (None, None, None)
    file_title = remaining_path[:-len('.html')]
    canonical_file_title = file_title.replace('.', '_')
    name = canonical_file_title + '.html'
    return (path + name, path2 + name, canonical_file_title != file_title)

def Handle404(response, doc_type = 'extensions'):
  response.status = 404
  response.write(Cache.get(NormalizePath(doc_type, '404.html')[0]))

class Handler(webapp2.RequestHandler):
  def get(self, doc_type, remaining_path):
    path, path2, need_redirect = NormalizePath(doc_type, remaining_path)
    if need_redirect:
      self.response.status = 302
      self.response.location = path
      return
    if REDIRECTS.get(path):
      self.response.status = 302
      self.response.location = REDIRECTS.get(path)
      return

    data = Cache.get(path)
    _AddSecurityHeaders(self.response)

    if data is None:
      if Cache.get(path2) is not None:
        self.response.status = 302
        logging.debug(path2)
        self.response.location = path2
      else:
        Handle404(self.response, doc_type)
    else:
      mimetypes.init()
      base, ext = os.path.splitext(remaining_path)
      self.response.content_type = mimetypes.types_map[ext]
      if doc_type == 'static':
        self.response.headers['Cache-Control'] = 'public, max-age=10800'
      else:
        pass
        # AppCache support is not yet ready.
        # data = data.replace('<html>', '<html manifest="/appcache.manifest">', 1)
      _AddCanonicalLinkHeader(path, self.response)
      self.response.write(data)

class ChannelRedirectHandler(webapp2.RequestHandler):
  def get(self, channel, realpath):
    self.response.location = '/' + realpath
    _AddSecurityHeaders(self.response)
    self.response.status = 301

class HomeRedirectHandler(webapp2.RequestHandler):
  def get(self):
    self.response.location = '/extensions/index.html'
    _AddSecurityHeaders(self.response)
    self.response.status = 301

class ExamplesRedirectHandler(webapp2.RequestHandler):
  def get(self, example_path):
    self.response.location = 'https://developer.chrome.com' + self.request.path
    _AddSecurityHeaders(self.response)
    self.response.status = 301

class AppsIndexRedirectHandler(webapp2.RequestHandler):
  def get(self, ):
    self.response.location = '/apps/about_apps.html'
    _AddSecurityHeaders(self.response)
    self.response.status = 301

class ExtensionsIndexRedirectHandler(webapp2.RequestHandler):
  def get(self, ):
    self.response.location = '/extensions/index.html'
    _AddSecurityHeaders(self.response)
    self.response.status = 301

class NotFoundHandler(webapp2.RequestHandler):
  def get(self):
    _AddSecurityHeaders(self.response)
    Handle404(self.response)

class APIUpdateHandler(webapp2.RequestHandler):
  # TODO: Store file listing so that 404 can be handled quickly.
  # TODO: Use task queues to avoid timeout.
  def post(self):
    try:
      api_data = json.loads(self.request.body)
      logging.info(api_data)
      if api_data.get('channel') == None:
        return
      channel = api_data.get('channel')
      path_prefix = api_data.get('path_prefix', '')
      files = api_data.get('files', [])
      for path in files:
        url = 'https://%s/_api/%s/render/%s/%s' % (
            os.environ.get('CRXDOCZH_SLAVE_DOCS_APP_DOMAIN'),
            os.environ.get('CRXDOCZH_SLAVE_DOCS_API_KEY'),
            channel,
            path_prefix + path)
        result = urlfetch.fetch(url, deadline = 60)
        if result.status_code == 200:
          Cache.update('/%s/%s%s' % (channel,
                                     path_prefix,
                                     path),
                       result.content)
        else:
          logging.error('Failed to request ' + path)
    except Exception as e:
      logging.error(e)

app = webapp2.WSGIApplication([
  (r'/_/api/' + os.environ.get('CRXDOCZH_MASTER_API_KEY') + '/pushUpdate',
      APIUpdateHandler),
  ('r/_cron/update', APIUpdateHandler),
  (r'/(trunk|dev|beta|stable)/?(.*)', ChannelRedirectHandler),
  (r'/extensions/examples/(.*)', ExamplesRedirectHandler),
  (r'/', HomeRedirectHandler),
  (r'/index.html', HomeRedirectHandler),
  (r'/apps/?', AppsIndexRedirectHandler),
  (r'/apps/index\.html', AppsIndexRedirectHandler),
  (r'/extensions/?', ExtensionsIndexRedirectHandler),
  (r'/(apps|extensions|static)/(.+)', Handler),
  (r'.*', NotFoundHandler)
])

