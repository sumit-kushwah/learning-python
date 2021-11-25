#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # Print the name of the OS
    print(os.name)

    # Check for item existence and type
    print(os.path.realpath('textfile.txt'))
    print(os.path.split(os.path.realpath('textfile.txt')))
    # Work with file paths

    # Get the modification time

    # Calculate how long ago the item was modified
    mod_time = datetime.datetime.fromtimestamp(
        os.path.getmtime('textfile.txt'))
    today = datetime.datetime.now()

    td = today - mod_time

    print(td.total_seconds())


if __name__ == "__main__":
    main()
