# Exercise 1
#
# 1.
# Proof that there are no positive numbers to satisfy a**n + b**n = c**n for n>2
#
# 2.
# Write a function that prompts the user to input values for a, b, c and n
# converts them to integers, and uses check_fermat to check wheter they violate
# Fermat's theorem

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

#2.


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
