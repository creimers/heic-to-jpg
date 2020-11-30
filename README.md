# `heic-to-jpg` 📸

CLI tool for converting `HEIC` images to `jpg`.

Essentially, this is just a wrapper around imagemagick's [`convert`](https://imagemagick.org/script/convert.php) cli.

Motivation: When transfering images from an iPhone to a Mac via airdrop, they are being transfered as `HEIC`. Oftentime though, another format (such as `jpg`) is required to further make use of those images.

## installation

`pip install heic-to-jpg`

## usage

`heic-to-jpg -s ~/path/to/source [--keep]`

or

`heic2jpg -s ~/path/to/source [--keep]`

`~/path/to/source` can both be a directory or a single `.HEIC` file. Without the `--keep` flag, the original file is deleted after conversion.
