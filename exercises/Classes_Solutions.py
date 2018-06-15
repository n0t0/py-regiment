print '\n Exercise 1\n'
# Exercise 1

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
print '\n Exercise 3\n'
# Exercise 3
# Write a version of move_rectangle that creates 
# and returns a new Rectangle instead of modifying the old one.
import copy 

# box2 = copy.deepcopy(box)

def mod_move_rectangle(rect, dx, dy):
    box2 = copy.deepcopy(box)
    box2.corner.x +=4 
    box2.corner.y +=6
    t = ()
    a = (box2.corner.x,) 
    b = box2.corner.y
    point = a + (b, )
    print point
    print box == box2 
mod_move_rectangle(box, box.corner.x, box.corner.y)
    



print '\n Exercise 4\n'
# Exercise 4
class Time(object):
    """
    Represents the time of the day.

    attributes: hour, minute, second
    """

t = Time()
t.hour = '%.2d' % 14
t.minute = '%.2d' % 9
t.second = '%.2d' % 23

def print_time(t):
    print '{}:{}:{}'.format(t.hour, t.minute, t.second)
print_time(t)


print '\n Exercise 6\n'
# Exercise 6

start = Time()
start.hour = 8
start.minute = 30
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 43
duration.second = 47

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >=60:
        sum.minute -= 60
        sum.hour += 1

    return sum
# done = add_time(start, duration)
# print_time(done)

# divide seconds until >60
import math
# from decimal import *


def increment(time, seconds):
    print_time(start)
    print seconds, 'seconds added'

    if seconds > 60:
        minutes = seconds / 60.00
        whole = minutes - minutes % 1
        print 'there are', int(math.floor(whole)), 'minutes in', seconds, 'seconds'
        time.minute += int(math.floor(whole))

        seconds = minutes % 1  * 60
        seconds = str(seconds).split('.')
        print int(seconds[0]), 'seconds are left over'
        time.second += int(seconds[0])

    else:
        time.second += seconds

    if time.second >= 60:
        time.second -= seconds
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1

    print_time(start)
increment(start, 411)


print '\n Exercise 8\n'

# t = Time()
# t.hour = '%.2d' % 14
# t.minute = '%.2d' % 9
# t.second = '%.2d' % 23
#
# class Time(object):
#     """
#     Represents the time of the day.
#
#     attributes: hour, minute, second
#     """
#     def __init__
#     # def print_time(self):
#     #     print '{}:{}:{}'.format(self.hour, self.minute, self.second)
#     # print_time(t)
#
#     def time_to_int(self):
#         minutes = self.hour * 60 + self.minute
#         seconds = minutes * 60 + self.second
#         return seconds
#
# t.time_to_int()
print '\n Exercise 9\n'

class Point(object):
    """
    Represent a point in 2D space
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def print_point(self):
        print '{}, {}'.format(self.x, self.y)
    # print_point(blank)

blank = Point()
blank = Point(2.0)
blank.print_point()

print '\n Exercise 10\n'

class Point(object):
    """
    Represent a point in 2D space
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{},{}'.format(self.x, self.y)


p = Point(3.0, 4.0)
print p


print '\n Exercise 11\n' 
# Exercise 11

class Point(object):
    """
    Represent a point in 2D space
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{},{}'.format(self.x, self.y)

    
    def add(self):
        pass
