# About

Build a Gameboy Advance executable that plays your favorite videos!

(Reminder: Put a screenshot/gif here)

# Dependencies

- bash interpreter
- [devkitPro gba-dev packages](https://devkitpro.org/wiki/Getting_Started)
- [ffmpeg](https://www.ffmpeg.org/)
- [Python 3](https://www.python.org/downloads/)


# Usage 

```bash

# Clone the repo 
git clone https://github.com/syndr-flora/gba-video-player
cd gba-video-player

# Download an mp4 file
wget https://github.com/Felixoofed/badapple-frames/raw/refs/heads/main/badapple.mp4

# Run the build script
chmod +x build.sh
./build.sh badapple.mp4

```

# Note

The current implementation of this program decodes the video into images _before_ the compile step. This inflates file sizes to be much higher than what a standard
cartridge can fit (16MB or 32MB). The max video length it can do without a rewrite is about 5 seconds.
