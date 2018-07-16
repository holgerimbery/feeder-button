#!/bin/bash
#
# script to generate the CCU addon package.

# generate tempdir
mkdir -p tmp/
rm -rf tmp/*

# copy all relevant stuff
cp -a update_script tmp/
cp -a VERSION tmp/
cp -a www tmp/
cp -a rc.d tmp/
cp -a profile.d tmp/
cp -a update_addon tmp/
cp -a config/*.cfg tmp/
cp -a config/*.cfg.template tmp/
cp -a update_cfg tmp/
cp -a URL tmp/


# generate archive
cd tmp
tar --exclude=.DS_Store -czvf ../feeder-button-$(cat ../VERSION).tar.gz *
#tar --owner=root --group=root --exclude=.DS_Store -czvf ../feeder-button-$(cat ../VERSION).tar.gz *
cd ..
rm -rf tmp
