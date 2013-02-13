# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

GITHUB_URL = 'https://api.github.com/repos/GoogleChrome/chrome-app-samples'
GITHUB_BASE = 'https://github.com/GoogleChrome/chrome-app-samples/tree/master'
RAW_GITHUB_BASE = ('https://github.com/GoogleChrome/chrome-app-samples/raw/'
                   'master')
OMAHA_PROXY_URL = 'http://omahaproxy.appspot.com/json'
SVN_URL_OFFICIAL = 'https://src.chromium.org/chrome'
SVN_URL = 'https://crxdoczh.googlecode.com/svn/trunk/chromium/crxdoczh'
VIEWVC_URL = 'http://src.chromium.org/viewvc/chrome'
SVN_TRUNK_URL = SVN_URL# + '/trunk'
SVN_BRANCH_URL = SVN_URL_OFFICIAL + '/branches'
OPEN_ISSUES_CSV_URL = (
    'http://code.google.com/p/chromium/issues/csv?can=1&'
    'q=Hotlist%3DKnownIssue%20Feature%3DApps+is%3Aopen')
CLOSED_ISSUES_CSV_URL = (
    'http://code.google.com/p/chromium/issues/csv?can=1&'
    'q=Hotlist%3DKnownIssue+Feature%3DApps+-is%3Aopen')
EXTENSIONS_SAMPLES = ('http://src.chromium.org/viewvc/chrome/trunk/src/chrome/'
                      'common/extensions/docs/examples/')

SLAVE_SAMPLES_APP_ID = '<REPLACE_WITH_YOUR_SAMPLES_APP_ID>'
SLAVE_SAMPLES_API_KEY = '<REPLACE_WITH_YOUR_SAMPLES_API_KEY>'
SLAVE_SAMPLES_API_BASE_URL = '_/api/' + SLAVE_SAMPLES_API_KEY + '/json/samples/'
    # Sample path: /[<channel>/]_/api/<api key>/json/samples/{apps|extensions}
