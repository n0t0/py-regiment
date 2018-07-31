# Return Values
import math

def area(radius):
    temp = math.pi * radius**2
    return temp # temporary variables make debugging easier

def area(radius):
    return math.pi * radius**2 # more concise structure


def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x


def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print 'dx is:', dx
    print 'dy is:', dy
    dsquared = dx**2 + dy**2
    print 'dsquared is:', dsquared
    result = math.sqrt(dsquared)
    return result

distance(1,2,4,6)


# Composition

xc = 2
yc = 3
xp = 4
yp = 6

radius = distance(xc, yc, xp, yp)
result = area(radius)


def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result


def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

# Boolean Functions

x = 4
y = 2

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

print is_divisible(4, 2)

# NOTE: the result is a boolean, so we can write it more concisely

def is_divisible(x ,y):
    return x % y == 0

# NOTE: boolean functions are often used in conditional statements

if is_divisible(x, y):
    print 'x is divisible by y'


def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

print factorial(3)


# Fibonacci

# fibonacci(0) = 0
# fibonacci(1) = 1
# fibonacci(n) = fibonacci(n-1)+fibonacci(n-2)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print fibonacci(8)


# Checking Types

def factorial(n):
    if not isinstance(n, int):
        print 'factorial is only defined for integers'
        return None
    elif n < 0:
        print 'factorial works only with positive integers'
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print factorial('farfuii')
print factorial(-3)


def ack(m, n):
    if n == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    return ack(m - 1, ack(m, n - 1))


print ack(3, 4)
