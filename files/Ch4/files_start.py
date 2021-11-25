#
# Read and write files using the built-in Python file methods
#

def main():
    # Open a file for writing and create it if it doesn't exist
    # f = open('textfile.txt', 'w+')

    # Open the file for appending text to the end
    f = open('textfile.txt', 'r')
    # write some lines of data to the file
    # for i in range(10):
    # f.write("This is line {}\n".format(i))

    # close the file when done
    # Open the file back up and read the contents
    if f.mode == 'r':
        fl = f.readlines()
        for line in fl:
            print(line, end="\n")
    f.close()


if __name__ == "__main__":
    main()
