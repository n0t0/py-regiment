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


class Rectangle(object):
    """Represents a rectangle.

    attrubutes: width, height, corner
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

center = find_center(box)
print_point(center)

# object are mutable

box.width = box.width + 50
box.height = box.height + 100


def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight


print box.width
print box.height

grow_rectangle(box, 50, 100)
print box.width
print box.height
