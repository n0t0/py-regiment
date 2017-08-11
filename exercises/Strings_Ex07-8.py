# Exercise 7
# There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method and
# write an invocation that counts the number of as in 'abracadabra'.

word = 'abracadabra'
print word.count('a')


# Exercise 8
# Read the documentation of the string methods at
# http://docs.python.org/2/library/stdtypes.html#string-methods.
# You might want to experiment with some of them to make sure you understand
# how they work. strip() and replace() are particularly useful.

# replace()

word = 'abracadabra'
print word.replace('a','-')
print word.replace('a','-', 2) # 3th argument counts occurences to be replaced

# strip()

w = 'Metallica - Unforgiven.mp4'
print w.strip('.mp4')

# The documentation uses a syntax that might be confusing.
# For example, in find(sub[, start[, end]]), the brackets indicate optional
# arguments. So sub is required, but start is optional, and if you include
# start, then end is optional.
