# Tuples are immutable

t = ('do','mi','sol')
print t

# to create a Tuple with a single element include final comma

t2 = ('la',)    # tuple
print type(t2)
x = ('na')      # string
print type(x)

# empty tuple()

t = tuple()
print t

# creating a sequence of elements

t = tuple('lizzard')    # string
print t
t2 = tuple([1,2,3,4,])  # list
print t2
t3 = tuple(('la','ti','do'))    # tuple
print t3

# most List operators work on Tuples
print t[2]
print t[2:4]
print t3[-1]

# Tuple assignment

# temp = a
# a = b
# b = temp
#
# a, b = b, a

addr = 'mika@na.na'
uname, domain = addr.split('@')
print uname
print domain

# Tuples as return values

t = divmod(7, 3) # dev() returns a tuple of two values
print t

quotient, remainder = divmod(7, 3)
print quotient
print remainder

def min_max(t):
    return min(t), max(t)

print min_max(t)
