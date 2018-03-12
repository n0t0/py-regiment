# Exercise 1
print '\nExercise 1\n'

# Python provides a built-in function called len that returns the length of a string,
# so the value of len('allen') is 5. Write a function named right_justify that takes
# a string named s as a parameter and prints the string with enough leading spaces so
# that the last letter of the string is in column 70 of the display.
#
# >>> right_justify('signature')
#                                                                  signature

s = 'signature'


def right_justify(s):
    print (70-len(s)) * ' ' + s

print right_justify(s)


string = 'today is a good day'
print len(string) * 2

# Exercise 2
print '\nExercise 2\n'

# A function object is a value you can assign to a variable or pass as an argument.
# For example, do_twice is a function that takes a function object as an argument
# and calls it twice:

# def do_twice(f):
#     f()
#     f()

# Here is an example that uses do_twice to call a function named print_spam twice.

# def print_spam():
#     print 'spam'
#
# do_twice(print_spam)

# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value,
#    and calls the function twice, passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes
#    a string as a parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'flood'
#    as an argument.
# 5. Define a new function called do_four that takes a function object and a value
#    and calls the function four times, passing the value as a parameter.
#    There should be only two statements in the body of this function, not four.

# 1

def do_twice(f):
    f()
    f()
    # print f
    # print f


def print_spam():
    print 'spam'

do_twice(print_spam)
print '----'*40

# 2

v = 'variable'
def do_twice(f, v):
    f(v)
    f(v)


def print_spam(v):
    print 'spam'

do_twice(print_spam, v)
print '----'*40

# 3

def print_twice(krakra):
    print krakra
    print krakra

print_twice('double trouble')
print '----'*40

# 4

def do_twice(f, v):
    f(v)
    f(v)


def print_twice(krakra):
    print krakra
    print krakra

do_twice(print_twice,'flood')
print '----'*40

# 5

trop = 'kappa'
def print_twice(krakra):
    print krakra
    print krakra

def do_four(op, trop):
    op(trop)
    op(trop)

do_four(print_twice, trop)

# Exercise 3
print '\nExercise 3\n'

# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence:
# print '+', '-'
# If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
# print '+',
# print '-'
# The output of these statements is '+ -'.
# A print statement all by itself ends the current line and goes to the next line.
#
# 2. Write a function that draws a similar grid with four rows and four columns.

# 1.
# Example 1

a = '+'
b = '-'
c = '|'
d = ' '


def square():
    print a,
    print b, b, b, b,
    print a,
    print b, b, b, b,
    print a
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print a,
    print b, b, b, b,
    print a,
    print b, b, b, b,
    print a
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print c,
    print d, d, d, d,
    print c,
    print d, d, d, d,
    print c
    print a,
    print b, b, b, b,
    print a,
    print b, b, b, b,
    print a

square()

# Example 2


def build_square(x, y):
    x()
    y()
    y()
    y()
    y()
    x()
    y()
    y()
    y()
    y()
    x()


def print_topBottom():
    print a, b, b, b, b, '+', b, b, b, b, '+'

def print_content():
    print c, d, d, d, d, '|', d, d, d, d, '|'

build_square(print_topBottom, print_content)

# Example 3

f = (a + (d + b)*4 + d) * 2 + a
g = (c + 9*d)*2 + c


def print_twice(a):
    print a
    print a

def do_twice(a,b):
    a(b)
    a(b)

def box():
    print f
    do_twice(print_twice, g)
    print f
    do_twice(print_twice, g)
    print f

box()

# 2.
# Example 1

a = '+'
b = '-'
c = '|'
d = ' '

f = (a + (d + b)*4 + d) * 4 + a
g = (c + 9*d)*4 + c


def print_twice(a):
    print a
    print a


def do_twice(a,b):
    a(b)
    a(b)


def box():
    print f
    do_twice(print_twice, g)
    print f
    do_twice(print_twice, g)
    print f
    do_twice(print_twice, g)
    print f
    do_twice(print_twice, g)
    print f

box()

# Example 2


def lines(line):
    print line


def buildBox(a, b):
    lines(f)
    for l in range(4):
        lines(g)
    lines(f)
    [lines(g) for l in range(4)]
    lines(f)
    [lines(g) for l in range(4)]
    lines(f)
    [lines(g) for l in range(4)]
    lines(f)

buildBox(lines, g)
