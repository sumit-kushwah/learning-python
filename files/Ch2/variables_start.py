#
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)


# re-declaring the variable works

f = 'abc'
print(f)

# ERROR: variables of different types cannot be combined

print('my name is sumit' + str(123))


# Global vs. local variables in functions

def hello():
    global f
    f = 'redef'
    print(f)


hello()
print(f)
