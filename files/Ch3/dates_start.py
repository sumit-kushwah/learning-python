#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
    # DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today = date.today()
    print(today)

    # print out the date's individual components
    print(today.day, today.year, today.month)
    # retrieve today's weekday (0=Monday, 6=Sunday)
    print(today.weekday())
    # DATETIME OBJECTS
    # Get today's date from the datetime class
    print(datetime.now())
    # Get the current time
    t = datetime.time(datetime.now())
    print(t)


if __name__ == "__main__":
    main()
