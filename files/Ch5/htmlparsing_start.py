#
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        global metacount
        if tag == "meta":
            metacount += 1

        print('encounterd a start tag:', tag)


def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()


if __name__ == "__main__":
    main()
