#!/bin/bash

rsync -a --exclude='.svn' --exclude='.git' --exclude='*.cc' --exclude='*.h' --exclude='server2' --exclude='server_static' --exclude='examples' ../official/src ./
svn status

