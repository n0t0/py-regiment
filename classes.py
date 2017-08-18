# User defined type is called a Class

from math import sqrt

class Point(object):
    """Represent a point in 2D space"""

print Point # Point is defined at top level so fullname is __main__

blank = Point() # instantination; blank is an instance of the class Point()
print blank

# attributes

blank.x = 3.0
blank.y = 4.0

print blank.y
x = blank.x
print x

# dot notation can be used with expressions

print '({}, {})'.format(blank.x, blank.y)
distance = sqrt(blank.x ** 2 + blank.y ** 2)
print distance

def print_point(p):
    print '{}, {}'.format(p.x, p.y)

print print_point(blank)

# instide the function p is an alias for blank;
# if the function changes p, blank changes
