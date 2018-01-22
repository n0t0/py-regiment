# Exercise 1
# Rewrite the function print_n using iteration instead of recursion.

def print_n(s, n):
    if n <= 0:
        return
    print s
    print print_n(s, n-1)

print print_n('flood', 5)

# Exercise 2
# Encapsulate this loop

while True:
    print x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y

# in a function called square_root that takes a as a parameter,
# chooses a reasonable value of x, and returns an estimate of
# the square root of a.
