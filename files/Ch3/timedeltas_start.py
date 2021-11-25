#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime, timedelta


# construct a basic timedelta and print it

td = timedelta(days=2, hours=12, seconds=12)
print(td)

# print today's date
print(datetime.now())

# print today's date one year from now
print(datetime.now() + timedelta(days=365))

# create a timedelta that uses more than one argument
td = timedelta(weeks=1)

# calculate the date 1 week ago, formatted as a string
result = datetime.now() - td
print(result.strftime('%d-%b-%Y'))

# How many days until April Fools' Day?
today = datetime.now()
afd = datetime(year=today.year, month=4, day=1)

if today > afd:
    print('April fool already passed {} days before'.format((today - afd).days))
    afd = afd.replace(year=today.year + 1)
    print('Next april fool in {} days'.format(
        (afd - today).days
    ))
else:
    print((afd - today).days, " days left in april fool")
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year


# Now calculate the amount of time until April Fool's Day
