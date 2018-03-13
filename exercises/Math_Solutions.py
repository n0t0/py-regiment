print '\n Exercise 1\n'
# Exercise 1
# Write a compare function that returns 1 if x > y, 0 if x == y,
# and -1 if x < y.

x = 2
y = 1

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        x < y
        return -1
print compare(x, y)

def check():
    return 1
check()


print '\n Exercise 2\n'
# Exercise 2
# Use incremental development to write a function called hypotenuse that returns
# the length of the hypotenuse of a right triangle given the lengths of the two
# legs as arguments. Record each stage of the development process as you go.

from math import sqrt

def hypotenuse(l1, l2):
    h = l1**2 + l2**2
    print sqrt(h)
hypotenuse(3, 4)


print '\n Exercise 3\n'
# Exercise 3


def is_between(x, y, z):
    return x <= y and y <= z
    #     return True
    # else:
    #     return False

print is_between(2,4,6)

# Exercise 4
print '\n Exercise 4\n'


# Exercise 5
print '\n Exercise 5\n'

word = 'racecar'

def is_palindrome(word):
    if word[::-1] == word[:]:
        print "It is a palindrome"
    else: 
        print "Try another word"
is_palindrome(word)



