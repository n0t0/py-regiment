# Just like a String, List is a Sequence of Values
# In a String, Values are Characters; in a List Values are Elements or Items

# The Elements of a List Don't Have to be From the Same type
print '===='*40

l = [40,50,60]
l2 = ['uno', 'dos', 'tres']
l3 = [2,3.0,'four',[5,6]] # a list within another list is nested
print l, l2, l3

l4 = [] # empty list

# Unlike a Strings; Lists are Mutable
print '===='*40

wine = ['Merlot', 'Pinot Noir', 'Cabernet Souvignon', 'Malbec', 'Zinfandel']
print wine[2] # indexing is done the same way as in strings
print wine[-1]

numbers = [20,30]
print numbers
numbers[1] = 40  #indexed element can be assigned
print numbers

# The in Operator Works as With Strings

print 'Merlot' in wine
print 'Chardonnay' in wine

# Traversing a List
print '===='*40

for w in wine:
    print wine


for i in range(len(numbers)): # len() returns the number of elements
    print numbers[i] * 2      # range() returns a list of indices

# List Operations
print '===='*40

a = [7,17,27]
b = [3, 13, 23]
c = a + b
print c

print [8] * 4
print [2, 12, 22] * 3

# List Slices
print '===='*40

scale = ['C','D','E','F','G','A','B','C']
print scale
print scale[2:5] # slice
print scale[:5]  # from beginning to index
print scale[3:]  # from index to end

# Since Lists are Mutable, It is a Good Practice to Copy Before Operate Them
print '===='*40

scale[2] = ['Eb']
scale[5:7] = [['Ab','Bb']]
print scale

# Map, filter, and reduce
print '===='*40

t = [1, 2, 3, 4, 5]

def add_all(t):
    total = 0
    for x in t:
        total += x # total = total + x
    return total

print sum(t) # built-in function to calculate sum

# Deleting Elements
print '===='*40

t = ['a', 'b', 'c']
x = t.pop(1) # pop() modifies the list and returns the removed element
print x
print t

t = ['a', 'b', 'c']
del t[1] # del returns the original list but the deleted item
print t

t.remove('a') # remove can be used by typing the element
print t

t = ['left', 'right', 'up', 'down', 'forward', 'backward']
del t[2:4] # deletes a slice
print t

# Lists and Strings
print '===='*40

s = 'string'
t = list(s) # list() convert a string into a list
print t


s = 'today is a good day'
t = s.split()
print t

s = 'today-is-a-good-day'
delimeter = '-'
t = s.split(delimeter) # split() can take a delimeter argument
print t

t = ['everyone', 'loves', 'music']
d = ' '
print d.join(t) # join() is a string method so it has to be invoked on delimeter

# Object and Values
print '===='*40

a = 'giraffe'
b = 'giraffe'

print a is b # python creates only one string Object

a = [1, 2, 3]
b = [1, 2, 3]

print a is b # two object for lists

# Aliasing
print '===='*40

a = [1, 2, 3]
b = a
print b

# NOTE: if an object is mutable; changes made with/to one alias affect the other

b[0] = 21
print a

# List Argument
print '===='*40

def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print letters

# Distinguish Between Modifying vs. Creating a List
print '===='*40

t1 = [1, 2]
t2 = t1.append(3) # append() modifies a list
print t1
print t2

t3 = t1 + [4] # + operator creates a list
print t3


def tail(t):
    return t[1:]

letters = ['a', 'b', 'c']
rest = tail(letters)
print rest
