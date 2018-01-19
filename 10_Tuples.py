# Tuples are Immutable

t = ('do','mi','sol')
print t

# To create a Tuple with a Single Element Include Final Comma

t2 = ('la',)    # tuple
print type(t2)
t3 = ('la','la') # tuple
print type(t3)
x = ('single item inside () is not a tuple')      # string
print type(x)

# Empty tuple()

t = tuple()
print t

# Creating a Sequence of Elements

t = tuple('lizzard')    # string
print t
t2 = tuple([1,2,3,4,])  # list
print t2
t3 = tuple(('la','ti','do'))    # tuple
print t3

# Most List Operators Work on Tuples
print t[2]
print t[2:4]
print t3[-1]

# Adding or Replacing a Tuple Element

t = tuple('gara')
print t
t = t[:] + ('ta',) # adding a tuple
print t
t = (' ',) + t[1:4]
print t

# Tuple Assignment

# temp = a
# a = b
# b = temp
#
# a, b = b, a

addr = 'mika@na.na'
print type(addr)
uname, domain = addr.split('@')
print uname
print domain

lyrics = 'All we need is just a little patience'
a, b = lyrics.split('just')
print a, b

# Tuples as Return Values

t = divmod(7, 3) # dev() returns a tuple of two values
print t

quotient, remainder = divmod(7, 3)
print quotient
print remainder


def min_max(t):
    return min(t), max(t)
print min_max(t)


# Variable-lenght Argument Tuples
# NOTE: * in front of a parameter will gather all arguments


def printall(*args):
    print args
print printall('$','100', 100, 100.00, 'dollars')
print type(printall)

# NOTE: * can scatter a sequence of values as multiple arguments

t = (8,3)
print type(t)
print divmod(*t) # divmod() requires 2 arguments

# Lists and Tuples

s = 'abc'
t = [0, 1, 2]
print zip(s, t)

print zip('Crocodile', 'Monkey') # zip results the shorter sequencer

t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print number, letter


# Dictionaries and Tuples

d = {'a':0, 'b':1, 'c':2}
print d.items() # items() returns a listh of tuples

t = [('a', 0), ('b', 1), ('c', 2)]
d = dict(t) # creating a dictionary from tuples
print d

d = dict(zip('abc', range(3))) # dict() + zip()
print d

lt = [('d', 4), ('e', 5)] # update() method
d.update(lt)
print d

for key, val in d.items():
    print val, key


last = 'Vardar'
first = 'Bego'
d = dict()
d[last,first] = 5557551428
print d

for last, first in d:
    print first, last, d[last,first]

# Comparing Tuples

print (0, 1, 2) < (0, 3, 4)
print (0, 1, 2000000) < (0, 3, 4)


words = ['dog', 'monkey', 'fly', 'crocodile', 'horse']

def sort_by_lenght(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
print sort_by_lenght(words)

# Sequences of Sequences
