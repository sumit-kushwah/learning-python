#
# Example file for working with loops
#

def main():
    x = 0

    # define a while loop
    while(x < 5):
        x += 1
        print(x)

    # define a for loop
    for i in range(5, 10):
        print(i)

    # use a for loop over a collection
    days = ['mon', 'tue', 'wed', 'thur', 'fri', 'sat', 'sun']
    for day in days:
        print(day)

    # use the break and continue statements
    for i in range(5, 10):
        if i == 7:
            break
        print(i)

    for i in range(5, 10):
        if i & 1:
            continue
        print(i)

    # using the enumerate() function to get index
    for index, day in enumerate(days):
        print(index, day)


if __name__ == "__main__":
    main()
