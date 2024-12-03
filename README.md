# `heic-to-jpg` 📸

CLI tool for converting `HEIC` images to `jpg`.

Essentially, this is just a thin convenience wrapper around imagemagick's `magick` cli.

Motivation: When transfering images from an iPhone to a Mac via airdrop, they are being transfered as `HEIC`. Oftentime though, another format (such as `jpg`) is required to further make use of those images.

👉 ⚠️ Please note that [imagemagick](https://imagemagick.org/script/download.php) is a prerequisite for this to work.

👉 ⚠️ Please note that this has been tested on macOS only. There might be issues on other operating systems ([Linux](https://github.com/creimers/heic-to-jpg/issues/1), [Windows](https://github.com/creimers/heic-to-jpg/issues/2)).

## installation

`pip install heic-to-jpg`

(`pip3 install heic-to-jpg` for some; an up-to-date-ish python3 is recommended.)

Install `heic-to-jpg<0.2.0` to use imagemagick's `convert` cli.

Install `heic-to-jpg>=0.2.0` to use imagemagick's `magick` cli.

## usage

`heic-to-jpg -s ~/path/to/source [--keep] [--debug None|Trace|All]`

or

`heic2jpg -s ~/path/to/source [--keep] [--debug None|Trace|All]` 

`~/path/to/source` can both be a directory or a single `.HEIC` file. Without the `--keep` flag, the original file is deleted after conversion.

## development

- `pip install -e .` to install the package in editable mode
- `pip install -r requirements-dev.txt` to install development dependencies
- `pytest` to run tests

### build release

- `rm -rf dist/` to clean up
- `python -m build` to build the package
- `twine upload dist/*` to upload to pypi
