# Exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

# Exercise 2
# Modify the program to fix this error.

# In Roberts McCloskey's book 'Make Way for Ducklings', the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs
# these names in order:

_prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print letter + suffix
    if prefixes == 'O':
        print letter + 'u' + suffix_

# The output is:
#
# Jack
# Kack
# Lack
# Mack
# Nack
# Oack
# Pack
# Qack
# Of course, that's not quite right because "Ouack" and "Quack" are misspelled.

# Exercise 3
# Modify find so that it has a third parameter, the index in word
# where it should start looking.def find(word, letter):

    _index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1_

# Exercise 4
# Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

_word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count_

# Exercise 5
# Rewrite this function so that instead of traversing the string,
# it uses the three-parameter version of find from the previous section.

# Exercise 6
# There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method and
# write an invocation that counts the number of as in 'abracadabra'.

_word = 'abracadabra'
print word.count('a')_


# Exercise 7
# Read the documentation of the string methods at
# http://docs.python.org/2/library/stdtypes.html#string-methods.
# You might want to experiment with some of them to make sure you understand
# how they work. strip() and replace() are particularly useful.

# replace()

_word = 'abracadabra'
print word.replace('a','-')
print word.replace('a','-', 2) # 3th argument counts occurences to be replaced_

# strip()

_w = 'Metallica - Unforgiven.mp4'
print w.strip('.mp4')_

# The documentation uses a syntax that might be confusing.
# For example, in find(sub[, start[, end]]), the brackets indicate optional
# arguments. So sub is required, but start is optional, and if you include
# start, then end is optional.
