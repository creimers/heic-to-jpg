# `heic-to-jpg` 📸

CLI tool for converting `HEIC` images to `jpg`.

Essentially, this is just a thin wrapper around imagemagick's [`convert`](https://imagemagick.org/script/convert.php) cli.

Motivation: When transfering images from an iPhone to a Mac via airdrop, they are being transfered as `HEIC`. Oftentime though, another format (such as `jpg`) is required to further make use of those images.

👉 ⚠️ Please note that [imagemagick](https://imagemagick.org/script/download.php) is a prerequisite for this to work.

👉 ⚠️ Please note that this has been tested on macOS only. There might be issues on other operating systems ([Linux](https://github.com/creimers/heic-to-jpg/issues/1), [Windows](https://github.com/creimers/heic-to-jpg/issues/2)).

## installation

`pip install heic-to-jpg`

## usage

`heic-to-jpg -s ~/path/to/source [--keep] [--debug None|Trace|All]`

or

`heic2jpg -s ~/path/to/source [--keep] [--debug None|Trace|All]` 

`~/path/to/source` can both be a directory or a single `.HEIC` file. Without the `--keep` flag, the original file is deleted after conversion.
