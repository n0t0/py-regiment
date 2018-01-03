print '####'*40
# Modulus operator
print '####'*40

print 7 / 2
print 7 % 2 # returns the remainder after division
print 21 % 3 # if % returns zero one number is divisble by another


# NOTE:
# extracting the right most digit from a number - x % 10 x(in base of 10)
# the last two digits - x % 100

print 128 % 10
print 1024 % 100

print '####'*40
# Booleans - returns True or False values
print '####'*40

print 4 == 4
print 4 == 5

print '####'*40
# Relational operators
print '####'*40

m = 4
n = 6

print m != n # m is NOT equal to n
print m > n  # m is greater than n
print m < n  # m is less than n
print m >= n # m is greater OR equal to n
print m <= n # m is less or equal to n

print '####'*40
# Logical operators - and, or, and not
print '####'*40

a = 4
print a > 0 and a < 5 # returns True if both are true

n = 9
print n%2 == 0 or n%3 == 0 # returns True if either is true

x = 2
y = 10

print not x > y # returns True if x > y is False

print '####'*40
# Conditional execution
print '####'*40

x = 2
if x > 0:
    print 'x is greater than 0'

if x < 0:
    pass    # pass is used when there is no statement in the body

print '####'*40
# Alternative execution
print '####'*40

x = 6
if x%2 == 0:
    print 'x is even number'
else:
    print 'x is odd number'

print '####'*40
# Chained conditionals
print '####'*40

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
    # NOTE: if there is a else clause(not required), it has to be at the end
    # else:
    #     print 'No answer provided!'

print draw_b('b')


print '####'*40
# Nested conditionals
print '####'*40

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

if x > 10 or x < 6:
    print 'x is less than 6 or more than 10'
