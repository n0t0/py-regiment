from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)

# for elt in range(4):
#     fd(bob, 100)
#     lt(bob)

# exercise 1 

'''
def square(t):
    for elt in range(4):
        fd(t, 50)
        lt(t)        
square(bob)
'''

# exercise 2

'''
def square(t, l):
    for elt in range(4):
        fd(t, l)
        lt(t)
square(bob, 150)
'''

# exercise 3

# def polygon(t, l, n):
#     for elt in range(360/n):
#         fd(t, l)
#         lt(t, n)
# polygon(bob, 30, 70)

def polygon(t, lenght, n):
    angle = 360.0 / n 
    for elt in range(n):
        fd(t, lenght)
        lt(t, angle)
# polygon(bob, lenght=30, n=7)

# exercise 4

import math

bob.delay = 0.01 


def circle(t, r):
    C = 2 * math.pi * r 
    n = int(C / 2) + 1
    lenght = C / n
    polygon(t, lenght, n)
# circle(bob, 50)
        
# exercise 5
# Refactoring 

def arc(t, lenght, angle):
    arc_lenght = 2 * math.pi * angle / 360 
    n = int(arc_lenght / 3) + 1 
    step_lenght = arc_lenght / n
    step_angle = float(angle) / n 

    for elt in range(n):
        fd(t, step_lenght)
        lt(t, step_angle)


def polyline(t, n, lenght, angle):
    for i in range(n):
        fd(t, lenght)
        lt(t, angle)


def polygon(t, lenght, n):
    angle = 360.0 / n 
    polyline(t, n, lenght, angle)


def arc(t, lenght, angle):
    arc_lenght = 2 * math.pi * angle / 360 
    n = int(arc_lenght / 3) + 1 
    step_lenght = arc_lenght / n
    step_angle = float(angle) / n 
    polyline(t, n, lenght, angle)


def circle(t, r):
    arc(t, r, 360)


wait_for_user()