# Exercise 1
#
# 1.
# Proof that there are no positive numbers to satisfy a**n + b**n = c**n for n>2
#
# 2.
# Write a function that prompts the user to input values for a, b, c and n
# converts them to integers, and uses check_fermat to check wheter they violate
# Fermat's theorem.

# 1.

a = 1
b = 1
c = 3
n = 3


def check_fermat(a, b, c, n):
    if a > 0 and b > 0 and c > 0 and n > 2:
        if sum((a**n, b**n)) == c**n:
            print 'True'
        else:
            print 'False! Fermat\'s theorem holds'
check_fermat(a, b, c, n)

# 2.


def check_fermat(a, b, c, n):
    print 'Test Fermat\'s theorem.'
    print 'Give a value for a: '
    a = int(raw_input())
    print 'Give a value for b: '
    b = int(raw_input())
    print 'Give a value for c: '
    c = int(raw_input())
    print 'Give a value for n: '
    n = int(raw_input())
    # inp = int(raw_input(a), raw_input(b), raw_input(c), raw_input(n))
    # a, b, c, n = [int(a), int(b), int(c), int(n)]
    if a > 0 and b > 0 and c > 0 and n > 2:
        if sum((a**n, b**n)) == c**n:
            print 'True'
        else:
            print 'False! Fermat\'s theorem holds'
check_fermat(a, b, c, n)


# Exercise 2

# If you are given three sticks, you may or may not be able to arrange them
# in a triangle. For example, if one of the sticks is 12 inches long and
# the other two are one inch long, it is clear that you will not be able
# to get the short sticks to meet in the middle. For any three lengths,
# there is a simple test to see if it is possible to form a triangle:

# If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle. Otherwise, you can. (If the sum of two
# lengths equals the third, they form what is called a "degemerate" triangle.)

# 1.
# Write a function named is_triangle that takes three integers as arguments,
# and that prints either "Yes" or "No," depending on whether you can or cannot
# form a triangle from sticks with the given lengths.

# 2.
# Write a function that prompts the user to input three stick lengths, converts
# them to integers, and uses is_triangle to check whether sticks with the given
# lengths can form a triangle.

# 1.


def is_triangle(a, b, c):
    if a > sum((b, c)) or b > sum((a, c)) or c > sum((b, a)):
        print 'No'
    else:
        print 'Yes'
is_triangle(2, 2, 5)

# 2.


def is_triangle(a, b, c):
    print 'Type a lenght for stick A'
    a = int(raw_input())
    print 'Type a lenght for stick B'
    b = int(raw_input())
    print 'Type a lenght for stick C'
    c = int(raw_input())
    if a > sum((b, c)) or b > sum((a, c)) or c > sum((b, a)):
        print 'No'
    else:
        print 'Yes'
is_triangle(a, b, c)
