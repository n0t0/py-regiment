class Time(object):
    """Represents the time of the day."""

    def print_time(t):
        print '{}:{}:{}'.format(t.hour, t.minute, t.second)


start = Time()
start.hour = 8
start.minute = 40
start.second = 50


# NOTE: There are to ways to call a method
Time.print_time(start) # functional syntax
start.print_time() # method syntax (more concise)


def time_to_int(t):
    minutes = t.hour * 60 + t.minute
    seconds = t.minute * 60 + t.second
    return seconds

def int_to_time(s):
    time = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return time



# __init__  and __str__ Methods

class Time(object):
    """
    Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def print_time(self):
        print str(self)

    def time_to_int(self):
        """Computes the number of seconds since midnight."""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)

time = Time()
time.print_time()
time = Time(9)
time.print_time()
time = Time (9, 45)
time.print_time()
time = Time (9, 45, 32)
time.print_time()
