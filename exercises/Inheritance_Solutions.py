print '\n Exercise 1 \n'

class Clock(object):
    
    cities = ['New York', 'London', 'Dubai', 'Tokyo']
    timezones = ['UTC']

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        
    
    # def time_to_int(self):
    #     minutes = self.hour * 60 + self.minute
    #     seconds = minutes * 60 + self.second
    #     return seconds
    #     print seconds
    
    # def __cmp__(self, other):
    #     # check hours 
    #     # if self.hour > other.hour: return 1 
    #     if self.hour > other.hour: print 'hour' 
    #     if self.hour < other.hour: return -1
    #     # if hours are tied - check minutes 
    #     if self.minute > other.minute: print 'minutes' 
    #     if self.minute < other.minute: return -1
    #     # if minutes are tied - check seconds 
    #     if self.second > other.second: return 1 
    #     if self.second < other.second: return -1 
    #     # exact same time
    #     return 0

    def print_time(self):
        print '{:02d}:{:02d}:{:02d}'.format(self.hour, self.minute, self.second)

    def __cmp__(self, other):
        t1 = self.hour, self.minute, self.second
        t2 = other.hour, other.minute, other.second
        return cmp(t1, t2)

t1 = Clock(11,4,2)
t2 = Clock(11,2,2)
t1.print_time()
t2.print_time()
   
print t1 > t2 

print '\n Exercise 1 \n'

