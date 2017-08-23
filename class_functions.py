class Time(object):
    """
    Represents the time of the day.

    attributes: hour, minute, second
    """

# time = Time()
# time.hour = '%.2d' % 14
# time.minute = '%.2d' % 9
# time.second = '%.2d' % 23

#Exercise 1
#Write a function called print_time that takes a Time
#object and prints it in the form hour:minute:second.
#Hint: the format sequence '%.2d' prints an integer using at least two digits,
#including a leading zero if necessary.



def print_time(Time):
    t = Time()
    t.hour = '%.2d' % 14
    t.minute = '%.2d' % 9
    t.second = '%.2d' % 23
    print '{}:{}:{}'.format(t.hour, t.minute, t.second)

print_time(Time)
