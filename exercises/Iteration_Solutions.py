from __future__ import division 
# Exercise 1
# Rewrite the function print_n using iteration instead of recursion.

def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)
print_n('flood', 5)


def print_n(s, n):
    while n != 0:
        print s
        n -= 1
print_n('spam', 5)

print '\nExercise 2\n'
# Exercise 2
# Encapsulate this loop,
#     if abs(y-x) < epsilon:
        # break:
# in a function called square_root that takes a as a parameter,
# chooses a reasonable value of x, and returns an estimate of
# the square root of a. Where epsilon = 0.0000001

# NOTE:
# while True:
#     print x
#     y = (x + a/x) / 2
#     if y == x:
#         break
#     x = y



epsilon = 0.0000001

# if abs(y-x) < epsilon:
#     print True

def square_root(a, x):
    while x > epsilon:
        print 'startin with x', x
        y = (x + a/x) / 2
        print 'y is', y
        if abs(y - x) < epsilon:
            print 'got it '
            break
        else:
            x = y
        print 'x is now', x        
square_root(9, 4)
