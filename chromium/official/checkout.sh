#!/bin/bash

svn checkout --depth=empty https://src.chromium.org/svn/trunk/src/ src
svn update --depth=empty src/{LICENSE,chrome{,/common{,/extensions}},ppapi,third_party,tools}
svn update src/{third_party/{handlebar,ply,simplejson},tools/json_{comment_eater,schema_compiler},ppapi/generators}
svn update src/chrome/common/extensions/{api,docs}
