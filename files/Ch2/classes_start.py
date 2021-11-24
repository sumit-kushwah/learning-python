#
# Example file for working with classes
#

class A:
    def method_first(self):
        print('this is class a and method one')

    def method_second(self):
        print('this is class a and method second')


class B(A):
    def method_first(self):
        print('this is class b and method one')

    def method_second(self):
        super().method_second()


def main():
    a = A()
    b = B()
    a.method_first()
    b.method_second()


if __name__ == "__main__":
    main()
