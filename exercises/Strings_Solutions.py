# Exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

x = 'unforgiven'

def backward(x):
    for char in x[::-1]:
        print char

backward(x)

# Exercise 2
# Modify the program to fix this error.

# In Roberts McCloskey's book 'Make Way for Ducklings', the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs
# these names in order:

prefixes = 'JKLMNOPQ'
suffix = 'ack'

"""
for letter in prefixes:
    print letter + suffix
    if prefixes == 'O':
        print letter + 'u' + suffix
"""

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
# Modify the program to fix this error.

for l in prefixes:
    if l in prefixes[5]:
        print l + 'uack'
    elif l in prefixes[7]:
        print l + 'uack'
    else:
        print l + suffix

# Exercise 3
# Modify find so that it has a third parameter, the index in word
# where it should start looking.

# NOTE: look <word>.find() for third argument

"""
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
print find('exercise','r')
"""


def find(word, letter, start):
    index = 0
    for i in word:
        while index < len(word):
            if index < start:
                index = start
                if start > len(word):
                    print "Lenght of the word is: " + str(len(word))
                elif word[start] == letter:
                    return start, letter
            elif word[index] == letter:
                return index, letter
            index += 1
        # start += 2
    # find(word, letter, start)
    print 'Did not found "' + letter + '" after index: ' + str(start)
find('bobona', 'o', 4)
print '----'*20

print 'exercise 5'

word = 'abracadabra'
letter = 'c'
start = 0


def count_s(f):
    c = 0
    for l in f:
        print l
        # c += 4
    # print c, l + '\'s are found'
    # print c
    # print letter
count_s(find(word, letter, start))

print '----'*20


def count(string, letter):
    c = 0
    for x in string:
        if x == letter:
            c += 1
    print c, letter + '\'s are found'
count('exercise', 'e')

print '\nExercise 4\n'
# Exercise 4
# Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count

s = 'Today is raining'
l = 'i'


def count(string, letter):
    c = 0
    for x in string:
        if x == letter:
            c += 1
    print c, letter + '\'s are found'
count('exercise', 'e')


print '\nExercise 5\n'
# Exercise 5
# Rewrite _count_ function so that instead of traversing the string,
# it uses the three-parameter version of _find_ from the previous section.

string = 'abracadabra'
letter = 'a'
start = 1
def count(*args):
    c = 0
    if find(string, letter, start) > 1:
        c += 1
        print letter
    else:
        print 'Letter not found'
    print str(c), letter + ' found'
count(find(string, letter, start))


print '\nExercise 6\n'
# Exercise 6
# There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method and
# write an invocation that counts the number of as in 'abracadabra'.


word = ' abracadabra'
print word.count('a')

print '\nExercise 7\n'
# Exercise 7

s = 'abracadabra.puff'
# str.strip()
print s.strip('.puff')

# str.replace()
print s.replace('puff', 'paff')

# str.endswith()
print s.endswith('abra',0, 4)

# str.find()
print s.find('bra', 2)

# str.lower()
print s.islower()

# str.split()
print s.split('ca')

print '\nExercise 8\n'
# Exercise 8

w = 'annapolis'
s = 'radar'
print s == s[::-1]
