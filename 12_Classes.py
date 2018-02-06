# User Defined Type is Called a Class

from math import sqrt

class Point(object):
    """
    Represent a point in 2D space
    """

print Point # point is defined at top level so fullname is __main__

blank = Point() # instantination; blank is an instance of the class Point()
print blank

# Attributes

blank.x = 3.0
blank.y = 4.0

print blank.y
x = blank.x
print x
# NOTE:
# Dot (.) notation can be used with expressions

print '({}, {})'.format(blank.x, blank.y)
distance = sqrt(blank.x ** 2 + blank.y ** 2)
print distance

def print_point(p):
    print '{}, {}'.format(p.x, p.y)
print print_point(blank)

# NOTE:
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

# Objects are mutable

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

# Copying is alternative to aliasing

p1 = Point()
p1.x = 3.0
p1.y = 4.0

import copy

p2 = copy.copy(p1)
print_point(p1)
print_point(p2)
print p1 is p2 # p1 and p2 contain the same data but are different points
print p1 == p2 # for instances '==' is the same as the 'is' operator


box2 = copy.copy(box)
print box2 is box
print box2.corner is box.corner

# NOTE:
# shallow copy copies object's references, but not embedded objects

# type(object) and hasattr(object, 'name-of-attribute')
