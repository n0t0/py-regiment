# Exercise 4

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

print print_twice('double trouble')
print '----'*40

# 4

def do_twice(f, v):
    f(v)
    f(v)


def print_twice(krakra):
    print krakra
    print krakra

print do_twice(print_twice,'flood')
print '----'*40

# 5

trop = 'kappa'
def print_twice(krakra):
    print krakra
    print krakra

def do_four(op, trop):
    op(trop)
    op(trop)

print do_four(print_twice, trop)
