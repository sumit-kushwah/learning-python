#
# Example file for retrieving data from the internet
#

import urllib.request


def main():
    webUrl = 'https://www.google.com'
    result = urllib.request.urlopen(webUrl)
    print(result.read())


if __name__ == "__main__":
    main()
