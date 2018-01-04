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
