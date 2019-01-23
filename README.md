### Installation

```
sudo pip install panasonic-concat
```

### Description

Util concats `*.MTS` files and improves an audio loudness. It's a typical pipeline done with video files on a panasonic video-cameras (like HC v770). Equivalent ffmpeg commands:

```bash
ffmpeg -i 'concat:0.MTS|1.MTS|2.MTS' -vcodec copy -acodec copy res.mp4
ffmpeg-normalize -v res.mp4 -c:a aac -b:a 384k -lrt 20 -tp 0 -o res.mp4
```

### Help

```
usage: panasonic-concat [-h] [-n] [-o FILE] path [path ...]

Convert a bunch of MTS files to a video with a normalized sound.

positional arguments:
  path             path to the MTS file(s)

optional arguments:
  -h, --help       show this help message and exit
  -n, --normalize  do the audio normalization
  -o FILE          the output file name, (record's date used by default)
```

### Examples

Pay attention, the current directory is used as a temprorary (so it's better to `cd` to the home dir). The typical usage example:

```bash
cd ~
panasonic-concat /sdcard/STREAM/{5,6,7,8}.MTS -o lecture.mp4
```

The output file name can be omitted, so the record's time (or the current time) like `2018-06-03__13-16-20.mp4` will be used:

```bash
panasonic-concat /sdcard/STREAM/5.MTS ../../6.MTS --normalize
```

### Dev notes

- [How to distribute the package to pip](https://packaging.python.org/tutorials/packaging-projects/)
- [Command line scripts](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html)
