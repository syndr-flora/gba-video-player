#!/bin/bash

if [ -z $1 ] ; then
    echo "Usage: $0 <filename.mp4>"
    exit 1
fi

if [ ! -f "$1" ]; then
    echo "$1 not found!"
    exit 1
fi

rm -rf graphics
mkdir -p graphics build

# ffmpeg -i "$1" -ss 00:01:00 -to 00:01:05 -vf scale="240:160" -r 30 graphics/frame_%04d.png
ffmpeg -i "$1" -vf scale="240:160" -r 30 graphics/frame_%04d.png
shopt -s nullglob; files=(graphics/*)
export NUM_FRAMES=${#files[@]}

python3 build_grit.py
python3 build_array.py
make
