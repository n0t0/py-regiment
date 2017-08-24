# Modulus operator

print 7 / 2
print 7 % 2 # returns the remainder after division

# NOTE:
# extracting the right most digit from a number - x % 10 x(in base of 10)
# the last two digits - x % 100

print 128 % 10
print 1024 % 100


# Booleans - returns True or False values

print 4 == 4
print 4 == 5

# Relational operators

m = 4
n = 6

print m != n # m is NOT equal to n
print m > n  # m is greater than n
print m < n  # m is less than n
print m >= n # m is greater OR equal to n
print m <= n # m is less or equal to n

# Logical operators - and, or, and not

a = 4
print a > 0 and a < 5 # returns True if both are true

n = 9
print n%2 == 0 or n%3 == 0 # returns True if either is true

x = 2
y = 10

print not x > y # returns True if x > y is False

# Conditional execution

x = 2
if x > 0:
    print 'x is greater than 0'

if x < 0:
    pass    # pass is used when there is no statement in the body

# Alternative execution

x = 6
if x%2 == 0:
    print 'x is even number'
else:
    print 'x is odd number'

# Chained conditionals

x = 4
y = 2
if x > y:
    print 'x is greater than y'
elif x < y:
    print 'x is less than y'
else:
    print 'x and y are equal'


def draw_b(a):
    if a == 'a':
        print 'The answer is A'
    elif a == 'b':
        print 'The answer is B'
    elif a == 'c':
        print 'The answer is C'
    else:
        print 'No answer provided!'

print draw_b('b')

# Nested conditionals

x = 2
y = 4

if x == y:
    print 'x and y are equal'
else:
    if x > y:
        print 'x is greater than y'
    else:
        print 'x is less than y'

# NOTE:
# Nested conditionals can be difficult to read; logical operators are better

x = 5
if 0 < x:
    if x < 10:
        print 'x is a positive number' # nested

if x > 0 and x < 10:
    print 'x is a positive number' # logical
