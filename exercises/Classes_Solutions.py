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

import copy 


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

print '\n Exercise 5\n'
# Exercise 5

t2 = copy.copy(t)
# print t2

def is_after(t1, t2):
    print print_time(t) is print_time(t2)
is_after(print_time, t2)
    

print '\n Exercise 6\n'
# Exercise 6

start = Time()
start.hour = 8
start.minute = 30
start.second = 1

duration = Time()
duration.hour = 1
duration.minute = 43
duration.second = 140

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

    print_time(sum)
add_time(start, duration)

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

print_time(start)


print '\n Exercise 7\n'
# Exercise 7

time = copy.deepcopy(start)


def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds
    print seconds
time_to_int(time)


def int_to_time(seconds):
    time = copy.deepcopy(start)
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    print_time(time)
    return time
int_to_time(31011)


def pure_increment(time, seconds):
    seconds += time_to_int(time)
    return int_to_time(seconds)
pure_increment(start, 120)


print '\n Exercise 8\n'
# Exercise 8

s = Time()
s.hour = 1
s.minute = 52
s.second = 40


def convert_increment(time, seconds):
    print_time(s) 
    done = time_to_int(s) + seconds
    int_to_time(done)
convert_increment(start, 300)


print '\n Exercise 9\n'
# Exercise 9

import datetime
from datetime import date
from datetime import timedelta

import time
import calendar


#1 
print date.today()

class Date(object):
      
    
    def __init__(self, weekday=0):
        self.weekday = weekday
        

    def print_weekday(self):
        d = {
            'Monday':0,
            'Tuesday':1,
            'Wednesday':2,
            'Thirsday':3,
            'Friday':4,
            'Saturday':5,
            'Sunday':6
            }

        for k, v in d.iteritems():
            if v == day.today:
                print k


    def next_birthday(self, birthday):
        # year = timedelta(days=365)
        # another_year = timedelta(week)
        age = date.today() - birthday
        print age
        print age.total_seconds()
        print age.total_seconds() / 86400 

        # for n in age:
        #     print age / 60 

        
        
day = Date()
day.today = date.today().weekday()
print day.print_weekday()

birthday = datetime.date(1987,4,17)
print day.next_birthday(birthday)



    # def print_weekDay(self, weekday, weekend):
    #     self.
# today = datetime.date(2018, 7, 6)
# print today
# print datetime.time()
# print date.fromtimestamp(time.time())

print '\n Exercise 10\n'
# Exercise 10


class Clock(object):
    

    def print_time(time):
        print '{}:{}:{}'.format(time.hour, time.minute, time.second)
    
    def time_to_int(time):
        minutes = time.hour * 60 + time.minute
        seconds = minutes * 60 + time.second
        return seconds
        print seconds

time = Clock()
time.hour = 1
time.minute = 40
time.second = 52

print time.print_time()
print time.time_to_int()


print '\n Exercise 11\n'
# Exercise 11


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
blank = Point(2.0, 4.0)
blank.print_point()

print '\n Exercise 12\n'
# Exercise 12

class Point(object):
    """
    Represent a point in 2D space
    """

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)


p = Point(3.0, 4.0)
print p


print '\n Exercise 13\n' 
# Exercise 13


# p2 = copy.deepcopy(p)
# print p
# p2 = Point(4.0, 5.0)
# print p2

# print sum(p + p2)
# print p2

# A = Point(3.3, 4.4)
# print A
# B = Point(2.2, 1.1)
# print B


class Point(object):
    """
    Represent a point in 2D space
    """

    
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    
    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    
    def __add__(self, other):
        A = self.x + other.x
        B = self.y + other.y
        return Point(A,B)


lenght = Point(3.3, 4.4)
widht = Point(2.2, 2.1)
print lenght + widht 







        
        

