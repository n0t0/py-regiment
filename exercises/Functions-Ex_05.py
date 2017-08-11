# This exercise can be done using only the statements and other features we have learned so far.
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

print square()

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
    # print a,
    print a, b, b, b, b, '+', b, b, b, b, '+'

def print_content():
    print c, d, d, d, d, '|', d, d, d, d, '|'


print build_square(print_topBottom, print_content)

# Example 3

f = (a + (d + b)*4 + d) * 2 + a
g = (c + 9*d)*2 + c


def print_twice(double):
    print double
    print double

def do_twice(f,duo):
    f(duo)
    f(duo)

def box():
    print f
    do_twice(print_twice, g)
    print f
    do_twice(print_twice, g)
    print f

print box()
