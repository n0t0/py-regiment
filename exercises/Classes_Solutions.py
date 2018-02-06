print '\n Exercise 1\n'
# Exercise 1
# Write a function called _distance_between_points_ that takes two _Points_
# as arguments and returns the distance between them.

from math import sqrt


class Point(object):
    """
    represents a point in 2D space
    """

blank = Point()
blank.x = 3.0
blank.y = 4.0

def distance_between_points(p1, p2):
    distance = sqrt(p1 ** 2 + p2 ** 2)
    print distance
distance_between_points(blank.x, blank.y)

# TODO: define a functions within a class Point/s(object)

print '\n Exercise 2\n'
# Exercise 2
# Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding dx
# to the x coordinate of corner and adding dy to the y coordinate of corner.


class Rectangle(object):
    """
    Represents a rectangle

    attributes: widht, height, corner
    """

box = Rectangle()
box.widht = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def move_rectangle(rect, dx, dy):
    p = Point()
    p.x = rect.corner.x + 2
    p.y = rect.corner.y + 2
    point = p.x, p.y
    print point
move_rectangle(box, box.corner.x, box.corner.y)
