# Exercise 1
# Write a function called distance_between_points that takes two Points
# as arguments and returns the distance between them.

from math import sqrt


def distance_between_points(p1, p2):
    distance = sqrt(p1 ** 2 + p2 ** 2)
    print distance

print distance_between_points(3.0, 4.0)



# Exercise 2
# Write a function named move_rectangle that takes a Rectangle and two numbers
# named dx and dy. It should change the location of the rectangle by adding dx
# to the x coordinate of corner and adding dy to the y coordinate of corner.
