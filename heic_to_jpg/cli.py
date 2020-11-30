import os
import sys
import subprocess

import click


# TODO delete originals
# TODO optimize


@click.command()
@click.option("--keep", is_flag=True, help="Keep original source image?")
@click.option(
    "--src",
    "-s",
    type=click.Path(exists=True),
    help="Source directory of images to process or path to single image",
    required=True,
)
def main(keep, src):
    # check for 'convert'
    try:
        cmd = ["which", "convert"]
        subprocess.check_output(cmd)
    except Exception:
        click.secho("Program 'convert' not found!", fg="red")
        return

    if os.path.isdir(src):

        ###########
        # DIRECTORY
        ###########

        image_to_convert = []
        for filename in os.listdir(src):
            if filename.endswith(".heic") or filename.endswith(".HEIC"):
                absolute_filename = os.path.join(src, filename)
                # convert_image(absolute_filename)
                image_to_convert.append(absolute_filename)

        pwd = os.getcwd()
        os.chdir(src)
        command = [
            "convert",
            "*.HEIC",
            "-set",
            "filename:base",
            "%[basename]",
            "%[filename:base].jpg",
        ]
        subprocess.call(command)
        os.chdir(pwd)

        # remove?
        if not keep:
            for filename in image_to_convert:
                os.remove(filename)
    elif src.endswith(".heic") or src.endswith(".HEIC"):

        #############
        # SINGLE FILE
        #############

        pwd = os.getcwd()
        src_folder = os.path.abspath(os.path.dirname(src))
        os.chdir(src_folder)
        command = [
            "convert",
            src,
            "-set",
            "filename:base",
            "%[basename]",
            "%[filename:base].jpg",
        ]
        subprocess.call(command)
        os.chdir(pwd)

        if not keep:
            os.remove(src)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
