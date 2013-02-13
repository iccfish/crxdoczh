#!/usr/bin/env python
# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os
import sys

# Add the original server location to sys.path so we are able to import
# modules from there.
SERVER_PATH = 'chrome/common/extensions/docs/server2'
if os.path.abspath(SERVER_PATH) not in sys.path:
  sys.path.append(os.path.abspath(SERVER_PATH))

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from handler import Handler

def main():
  run_wsgi_app(webapp.WSGIApplication([('/.*', Handler)], debug=False))

if __name__ == '__main__':
  # HACK
  import sys
  reload(sys)
  sys.setdefaultencoding("utf-8")
  main()
