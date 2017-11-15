# Built in Functions

print int('32') # converts to integer
print int(32.99) # chops the fraction part
print int(-2.44)
print float(32) # converts to floating-point numbers
print str(32) # converts to string
print str(32.22)

# Math Functions
print '####'*40

# NOTE: Add Math's module and functions in another chapter
# Engine compression
# RPM
# AVG speed
# Aerodynamics
# Bike suspension

import math
print math

# ratio = signal_power / noise_power
# decibels = 10 * math.log10(ratio)
#
# radians = 0.7
# height = maht.sin(radians)
#
# degrees = 15
# radians = degrees / 360.0 * 2 * math.pi
# math.sin(radians)
#
# # check
#
# math.sqrt(2) / 2.0

#### Composition
# An argument of a function can be an expression or even a function calls
#
# x = time(3600 + 43)
# y = type(x)

# Keyword 'def' for Define a function
print '####'*40

def lyrics():
    print 'Go, tell Aunt Rhodie,'
    print 'go, tel Aunt Rhodie.'
    print 'Go, tell Aunt Rhodie, the'
    print 'goose is in her bed!'

print lyrics()
print type(lyrics)

# Calling a functions inside another function
print '####'*40

def variation():
    print lyrics()
    print 'Hurry, tell Aunt Rhodie, oh, plase'
    print 'hurry tell Aunt Rhodie.'
    print 'Hurry, tell Aunt Rhodie that the'
    print 'goose is in her bed. (Quack, quack!)'

print variation()

# Flow of execution
print '####'*40

def first():
    print 'This is the 1st function'
    print fourth()

def second():
    print 'This is the 2nd function'

def third():
    print 'This is the 3rd function'
    print first()

def fourth():
    print 'This is the 4th function'
    print second()

print third()

# NOTE: Parameters vs. Arguments
# Inside a function arguments are assigned to variables called parameters

def repeat(x): # argument
    print x # parameter
    print x # parameter

print repeat('s')
print repeat(2)
y = 3
print repeat(y)

# Local variables and parameters

def cat_repeat(part1, part2):
    cat = part1 + part2
    print repeat(cat)

print cat_repeat(2, 2)

line1 = 'King of the land! King of the land!'
line2 = 'Beast of the jungle say he is so grand!'
print cat_repeat(line1, line2)
