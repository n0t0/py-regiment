# Built in Functions

print int('32') # converts to integer
print int(32.99) # chops the fraction part
print int(-2.44) # same when negative numbers are involved
print float(32) # converts to floating-point numbers
print str(32) # converts to string
print str(32.22)

# More Built-In Functions

i = 1
print isinstance(i, int)

s = 'string'
print isinstance(s, str)
print isinstance(s, int)

# Math Functions
# NOTE: module --> colletion of functions

import math # importing a module

print math # prints information about it
print math.pi # calling a module's functions (dot notation)
print math.sqrt(16)

# Composition
# NOTE:  an argument of a function can be an expression or even a function call

print math.sqrt(2+2)
print math.sqrt(math.sqrt(16))



# Defining a Function; Keyword 'def'

def lyrics():
    print 'Go, tell Aunt Rhodie,'
    print 'go, tel Aunt Rhodie.'
    print 'Go, tell Aunt Rhodie, the'
    print 'goose is in her bed!'

print lyrics # defining a functions creates a variable with the same name
print type(lyrics) # and it has the type 'function'

print lyrics() # calling a function is the same as calin built-in function

# Calling a functions inside another function

def variation():
    print lyrics()
    print 'Hurry, tell Aunt Rhodie, oh, plase'
    print 'hurry tell Aunt Rhodie.'
    print 'Hurry, tell Aunt Rhodie that the'
    print 'goose is in her bed. (Quack, quack!)'

print variation()

# Flow of Execution;
# NOTE: follow the flow instead of reading top-bottom!

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


# Parameters vs. Arguments
# NOTE: inside a function arguments are assigned to variables called parameters


def repeat(x): # argument asiggned to a parameter inside the function
    print x # parameter
    print x # parameter

print repeat('s')
print repeat(2)
y = 3 # variable can be used as an argument
print repeat(y)

# Local Variables and Parameters


def cat_repeat(part1, part2):
    cat = part1 + part2
    print repeat(cat)

print cat_repeat(2, 2) # cat is destroyed when cat_repeat terminates

line1 = 'King of the land! King of the land!'
line2 = 'Beast of the jungle say he is so grand!'
print cat_repeat(line1, line2)
