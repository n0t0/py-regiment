# Return Values
import math

def area(radius):
    temp = math.pi * radius**2
    return temp # temporary variables make debugging easier

def area(radius):
    return math.pi * radius**2 # more concise structure


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print 'dx is:', dx
    print 'dy is:', dy
    dsquared = dx**2 + dy**2
    print 'dsquared is:', dsquared
    result = math.sqrt(dsquared)
    return result

distance(1,2,4,6)


# Composition


xc = 2
yc = 3
xp = 4
yp = 6

radius = distance(xc, yc, xp, yp)
result = area(radius)


def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))
