# Exercise 1

# Python provides a built-in function called len that returns the length of a string,
# so the value of len('allen') is 5. Write a function named right_justify that takes
# a string named s as a parameter and prints the string with enough leading spaces so
# that the last letter of the string is in column 70 of the display.
#
# >>> right_justify('signature')
#                                                                  signature

s = 'signature'


def right_justify(s):
    print (70-len(s)) * ' ' + s

print right_justify(s)


string = 'today is a good day'
print len(string) * 2

# Exercise 2
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
