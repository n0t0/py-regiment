## Exercise 1
#
# Write a function called do_n that takes a function object
# and a number, n, as arguments, and that calls the given function n times.

steps = 5

def walking():
    print 'Walking {} steps'.format(steps)

def do_n(w, steps):
    if steps <= 0:
        print 'Stop!'
    else:
        walking()
        do_n(walking, steps-1)

print do_n(walking, steps)

## Exercise 2
#
# Re-write the function above to indicate correctly the number of steps


