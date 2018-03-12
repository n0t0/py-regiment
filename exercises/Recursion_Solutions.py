## Exercise 1
print '\nExercise 1\n'
# Write a function called do_n that takes a function object
# and a number, n, as arguments, and that calls the given function n times.


def f_obj():
    print 'print object'

def do_n(f_obj, n):
    while n > 0:
        f_obj()
        n -=1
do_n(f_obj, 3)


## Exercise 2
print '\nExercise 2\n'
# Write a function that counts down how many times is being called 

steps = 5

def move():
    print 'Your turn!'

def do_n(move, steps):
    while steps > 0:
        if steps == 1:
            print '1 step left!'
            print 'No moves left!'
            break
        print steps, 'steps left'
        move()
        # do_n(move, steps)
        steps -= 1
do_n(move, steps)