#
# Example file for working with functions
#

# define a basic function
def hello():
    print('Hello world!')

# function that takes arguments


def displayName(name):
    print(f'My name is {name}')

# function that returns a value


def cube(x):
    return x * x * x

# function with default value for an argument


def power(x, r=1):
    result = 1
    for i in range(r):
        result *= x
    return result

# function with variable number of arguments


def sum_nums(*args):
    result = 0
    for arg in args:
        result += arg
    return result


hello()
displayName('sumit kushwah')
print(cube(5))
print(power(2, 3))
print(sum_nums(1, 2, 3, 4, 5, 6))
