print '====1'*40
# Exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

x = 'unforgiven'


def backward(x):
    for char in x[::-1]:
        print char
backward(x)


print '====2'*40
# Exercise 2
# Modify the program to fix this error.

# In Roberts McCloskey's book 'Make Way for Ducklings', the names of the ducklings
# are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs
# these names in order:

prefixes = 'JKLMNOPQ'
suffix = 'ack'


for letter in prefixes:
    print letter + suffix
    if prefixes == 'O':
        print letter + 'u' + suffix


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


for l in prefixes:
    if l in prefixes[5]:
        print l + 'uack'
    elif l in prefixes[7]:
        print l + 'uack'
    else:
        print l + suffix


print '====3'*40
# Exercise 3
# Modify find so that it has a third parameter, the index in word
# where it should start looking.

# NOTE: look <word>.find() for third argument


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
print find('exercise','r')


# v2


def find(word, letter, start):
    index = 0
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
    # return -1
    print 'Did not found "' + letter + '" after index: ' + str(start)
print find('exercise','r', 4)


print '====4'*40
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
    print c, letter
count('exercise', 'x')


print '====5'*40
# Exercise 5
# Rewrite _count_ function so that instead of traversing the string,
# it uses the three-parameter version of _find_ from the previous section.


# def count(string, letter, start):
#     c = 0
#     # find(string, letter, start)
#     find(string, letter, start)
#         c += 1
#         print c, i
# count('string', 'g', 1)


print '====6'*40
# Exercise 6
# There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method and
# write an invocation that counts the number of as in 'abracadabra'.


word = ' abracadabra'
print word.count('a')

print '====7'*40
# Exercise 7

s = 'abracadabra'
# str.endswith()
print s.endswith('abra',0, 4)

# str.find()
print s.find('bra', 2)

# str.lower()
print s.islower()

# str.split()
print s.split('ca')

print '====8'*40


# Exercise 8

w = 'annapolis'
s = 'radar'
print [s == s[::-1]]
