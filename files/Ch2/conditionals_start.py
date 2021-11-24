#
# Example file for working with conditional statements
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        print('x is less than y')
    elif x == y:
        print('x is same as y')
    else:
        print('x is greter than y')
    # conditional statements let you use "a if C else b"
    st = 'x gt y' if x > y else 'x is less or same as y'
    print(st)


if __name__ == "__main__":
    main()
