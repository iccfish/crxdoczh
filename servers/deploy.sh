#!/bin/bash

APPENGINE_PATH=~/google_appengine
APPENGINE_APPCFG="$APPENGINE_PATH/appcfg.py --oauth2"
KEYS_SED=private/keys.sed
CP='rsync -a --exclude=.svn --exclude=test_data'

prepare_keys () {
  cat > $KEYS_SED << END_OF_SED
#!/bin/sed -f
s#<REPLACE_WITH_YOUR_MASTER_API_KEY>#`cat private/MASTER_API_KEY`#
s#<REPLACE_WITH_YOUR_DOCS_APP_ID>#`cat private/SLAVE_DOCS_APP_ID`#
s#<REPLACE_WITH_YOUR_DOCS_API_KEY>#`cat private/SLAVE_DOCS_API_KEY`#
s#<REPLACE_WITH_YOUR_SAMPLES_APP_ID>#`cat private/SLAVE_SAMPLES_APP_ID`#
s#<REPLACE_WITH_YOUR_SAMPLES_API_KEY>#`cat private/SLAVE_SAMPLES_API_KEY`#
s#<REPLACE_WITH_YOUR_GITHUB_API_USERNAME>#`cat private/GITHUB_API_USERNAME`#
s#<REPLACE_WITH_YOUR_GITHUB_API_PASSWORD>#`cat private/GITHUB_API_PASSWORD`#
END_OF_SED
}

deploy_slave () (
  COMMON=slave-common
  SRC=slave-$1
  DST=slave-deploy

  mkdir $DST
  $CP $COMMON/* $DST/
  $CP $SRC/* $DST/
  sed -f $KEYS_SED $COMMON/url_constants.py > $DST/url_constants.py
  sed -f $KEYS_SED $SRC/app.yaml > $DST/app.yaml

  $DST/build_server.py
  rm $DST/build_server.py
  rm $DST/diff-chromium.sh
  $APPENGINE_APPCFG update $DST
  $APPENGINE_APPCFG backends update $DST
  rm -rf $DST
)

deploy_master () {
  SRC=master
  SRC_MIRROR=master-mirror
  DST=master-deploy

  mkdir $DST
  $CP $SRC/* $DST/
  if [ "$1" == mirror ]; then
    $CP $SRC_MIRROR/* $DST/
  fi
  sed -f $KEYS_SED $DST/app.yaml > $DST/app.yaml.1
  mv $DST/app.yaml.1 $DST/app.yaml

  $APPENGINE_APPCFG update $DST

  rm -rf $DST
}

prepare_keys

if [ "$1" == samples ]; then
  deploy_slave samples
fi

if [ "$1" == docs ]; then
  deploy_slave docs
fi

if [ "$1" == master ]; then
  deploy_master
fi

if [ "$1" == "master-mirror" ]; then
  deploy_master mirror
fi

