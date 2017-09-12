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
