# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value,
#    and calls the function twice, passing the value as an argument.
# 3. Write a more general version of print_spam, called print_twice, that takes
#    a string as a parameter and prints it twice.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam'
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

# 2

v = 'variable'
def do_twice(f, v):
    f(v)
    f(v)


def print_spam(v):
    print 'spam'

do_twice(print_spam, v)

# 3

def print_twice(krakra):
    print krakra
    print krakra

print print_twice('double trouble')

# 4

def do_twice(f, v):
    f(v)
    f(v)


def print_twice(krakra):
    print krakra
    print krakra

print do_twice(print_twice,'spam')

# 5

def print_twice(krakra):
    print krakra
    print krakra

def do_four(op, trop):
    op(trop)
    op(trop)

print do_four(print_twice, 'kappa')
