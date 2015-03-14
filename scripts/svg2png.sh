#!/usr/bin/env bash

# Convert SVG flag image files to optimized PNG files.
# You'll need svgexport and pngcrush:
#
#    https://www.npmjs.com/package/svgexport
#    https://www.npmjs.com/package/pngcrush-bin
#    
# SVG images are expected to be in ../flags/svg/
# and will be put in ../flags/png/.

SVG_FILES=../flags/svg/*
PNG_DIR=../flags/png/
RENDER_SIZE='1200:'
PNGCRUSH_OPTS='-ow -fix -reduce -force -nofilecheck -rem alla -oldtimestamp'

cd ${0%/*}

for svg_p in $SVG_FILES
do
  svg_n=${svg_p##*/}    # svg filename (from svg path)
  base_n=${svg_n%.*}    # basename
  png_n=$base_n".png"   # png filename
  png_p=$PNG_DIR$png_n  # png path
  
  echo "Converting $svg_p to $png_p."
  svgexport "$svg_p" "$png_p" $RENDER_SIZE > /dev/null 2>&1
  echo "Optimizing $png_p."
  pngcrush $PNGCRUSH_OPTS "$png_p" > /dev/null 2>&1
done
