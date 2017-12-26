class Time(object):
    """
    Represents the time of the day.

    attributes: hour, minute, second
    """

t = Time()
t.hour = '%.2d' % 14
t.minute = '%.2d' % 9
t.second = '%.2d' % 23

def print_time(t):
    print '{}:{}:{}'.format(t.hour, t.minute, t.second)

print_time(t)

# Pure Functions

def add_time(t1, t2): # prototype
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    return sum

start = Time()
start.hour = 8
start.minute = 30
start.second = 0

duration = Time()
duration.hour = 1
duration.minute = 43
duration.second = 47

done = add_time(start, duration)
print_time(done)

# Patching add_time() to carry minutes and seconds >60

def add_time(t1, t2):
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1

    if sum.minute >=60:
        sum.minute -= 60
        sum.hour += 1

    return sum

done = add_time(start, duration)
print_time(done)


# Modifiers

def increment(time, seconds):
    time.second += seconds

    if time.second >= 60:
        time.second -= 60
        time.minute += 1

    if time.minute >= 60:
        time.minute -= 60
        time.hour += 1



# NOTE: What happens if the parameter seconds is much greater than sixty?

# In that case, it is not enough to carry once; we have to keep doing it until
# time.second is less than sixty. One solution is to replace the if statements
# with while statements. That would make the function correct, but not very efficient.


def time_to_int(t):
    minutes = t.hour * 60 + t.minute
    seconds = t.minute * 60 + t.second
    return seconds


def int_to_time(seconds):
    time = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return time
