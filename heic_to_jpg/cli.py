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
@click.option(
    "--debug",
    default="None",
    help="Print convert debug info",
    type=click.Choice(["None", "Trace", "All"], case_sensitive=False),
)
def main(keep, src, debug):
    # check for 'convert'
    try:
        cmd = ["which", "convert"]
        subprocess.check_output(cmd)
    except Exception:
        click.secho("Program 'convert' not found!", fg="red")
        return

    image_to_convert = []
    if os.path.isdir(src):
        ###########
        # DIRECTORY
        ###########
        for filename in os.listdir(src):
            if filename.lower().endswith(".heic"):
                absolute_filename = os.path.join(src, filename)
                image_to_convert.append(absolute_filename)
        target = "*.[hH][eE][iI][cC]*"
        src_dir = src
    elif src.lower().endswith(".heic"):
        #############
        # SINGLE FILE
        #############
        target = src
        image_to_convert.append(src)
        src_dir = os.path.abspath(os.path.dirname(src))

    pwd = os.getcwd()
    os.chdir(src_dir)

    command = [
        "convert",
        "-debug",
        debug,
        target,
        "-set",
        "filename:base",
        "%[basename]",
        "%[filename:base].jpg",
    ]
    if debug in ("Trace", "All"):
        print(f"{command=}")
    subprocess.call(command)
    if os.path.isdir(src):
        os.chdir(pwd)

    # remove?
    if not keep:
        for filename in image_to_convert:
            os.remove(filename)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
