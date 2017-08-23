# Exercise 1
# Write a function called print_time that takes a Time object and prints it
# in the form hour:minute:second. Hint: the format sequence '%.2d' prints
# an integer using at least two digits, including a leading zero if necessary.

class Time(object):
    """
    Represents the time of the day.

    attributes: hour, minute, second
    """

def print_time(Time):
    t = Time()
    t.hour = '%.2d' % 14
    t.minute = '%.2d' % 9
    t.second = '%.2d' % 23
    print '{}:{}:{}'.format(t.hour, t.minute, t.second)

print_time(Time)

# Exercise 2
# Write a boolean function called is_after that takes two Time objects,
# t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise.
# Challenge: don't use an if statement 
