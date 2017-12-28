print '####'*40
# Built in Functions
print '####'*40


print int('32') # converts to integer
print int(32.99) # chops the fraction part
print int(-2.44) # same when negative numbers are involved
print float(32) # converts to floating-point numbers
print str(32) # converts to string
print str(32.22)


print '####'*40
# Math Functions
# Calling a 'dot notation' function from a module
# module - colletion of functions
print '####'*40


import math # importing a module

print math # prints information about it
print math.pi # calling a module's functions (dot notation)
print math.sqrt(16)


print '####'*40
# Composition
# An argument of a function can be an expression or even a function call
print '####'*40


print math.sqrt(2+2)
print math.sqrt(math.sqrt(16))


print '####'*40
# Define a function; Keyword 'def'
print '####'*40


def lyrics():
    print 'Go, tell Aunt Rhodie,'
    print 'go, tel Aunt Rhodie.'
    print 'Go, tell Aunt Rhodie, the'
    print 'goose is in her bed!'

print lyrics # defining a functions creates a variable with the same name
print type(lyrics) # and it has the type 'function'

print lyrics() # calling a function is the same as calin built-in function


print '####'*40
# Calling a functions inside another function
print '####'*40


def variation():
    print lyrics()
    print 'Hurry, tell Aunt Rhodie, oh, plase'
    print 'hurry tell Aunt Rhodie.'
    print 'Hurry, tell Aunt Rhodie that the'
    print 'goose is in her bed. (Quack, quack!)'

print variation()


print '####'*40
# Flow of execution; follow the flow instead of reading top-bottom!
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


print '####'*40
# NOTE: Parameters vs. Arguments
# Inside a function arguments are assigned to variables called parameters
print '####'*40


def repeat(x): # argument asiggned to a parameter inside the function
    print x # parameter
    print x # parameter

print repeat('s')
print repeat(2)
y = 3 # variable can be used as an argument
print repeat(y)


print '####'*40
# Local variables and parameters
print '####'*40


def cat_repeat(part1, part2):
    cat = part1 + part2
    print repeat(cat)

print cat_repeat(2, 2) # cat is destroyed when cat_repeat terminates


line1 = 'King of the land! King of the land!'
line2 = 'Beast of the jungle say he is so grand!'
print cat_repeat(line1, line2)
