#!/bin/bash
set -x

mkdir -p installation/dockercompose/src/
cp -R src/* installation/dockercompose/src/

tar -cvf build.tar installation/ --exclude=vagrant