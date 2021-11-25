#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil


def main():
    # make a duplicate of an existing file
    if path.exists("textfile.txt"):
        # get the path to the file in the current directory

        src = path.realpath('textfile.txt')

        dir, filename = path.split(src)

        # let's make a backup copy by appending "bak" to the name

        # copy over the permissions, modification times, and other info

        # dst = src + ".bak"

        # shutil.copy(src, dst)

        # rename the original file

        # os.rename('textfile.txt', 'newfile.txt')

        # now put things into a ZIP archive
        print(dir)
        shutil.make_archive("archive", "zip", dir)

        # more fine-grained control over ZIP files


if __name__ == "__main__":
    main()
