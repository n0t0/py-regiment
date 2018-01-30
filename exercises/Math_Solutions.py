# Exercise 1
# Write a compare function that returns 1 if x > y, 0 if x == y,
# and -1 if x < y.

x = 2
y = 1

def compare():
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        x < y
        return -1

compare()

def check():
    return 1

check()

# Exercise 2
# Use incremental development to write a function called hypotenuse that returns
# the length of the hypotenuse of a right triangle given the lengths of the two
# legs as arguments. Record each stage of the development process as you go.

from math import sqrt

def hypotenuse(l1, l2):
    h = l1**2 + l2**2
    print sqrt(h)

hypotenuse(4, 2)

# Exercise 3


def is_between(x, y, z):
    return x <= y and y <= z
    #     return True
    # else:
    #     return False

print is_between(2,4,6)
