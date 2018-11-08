# Exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.
print '\nExercise 1\n'

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
print '\nExercise 2\n'

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
print '\nExercise 3\n'

# NOTE: look <word>.find() for third argument

'''
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
print find('exercise','r')
'''


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
        # start += 1
    # find(word, letter, start)
    print 'Did not found "' + letter + '" after index: ' + str(start)
    return word, letter
    print word, letter


print find('bobona', 'o', 0)


# Exercise 4
# Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.
print '\nExercise 4\n'

'''
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count
'''


def count(string, letter):
    c = 0
    for x in string:
        if x == letter:
            c += 1
    print c, letter + '\'s are found'


count('exercise', 'e')


# Exercise 5
# Rewrite _count_ function so that instead of traversing the string,
# it uses the three-parameter version of _find_ from the previous section.
print '\nExercise 5\n'


word = 'exercise'
letter = 'e'
index = 0


def count_mod(word, letter, index):
    c = 0
    while index < len(word):
        if word[index] == letter:
            c += 1
            print index, letter
            print c, "occurance"
            # return index, letter
        index += 1


count_mod(word, letter, index)


# Exercise 6
# There is a string method called count that is similar to the function
# in the previous exercise. Read the documentation of this method and
# write an invocation that counts the number of as in 'abracadabra'.
print '\nExercise 6\n'


word = ' abracadabra'
print word.count('a')

# Exercise 7
print '\nExercise 7\n'

s = 'abracadabra.puff'
# str.strip()
print s.strip('.puff')

# str.replace()
print s.replace('puff', 'paff')

# str.endswith()
print s.endswith('abra', 0, 4)

# str.find()
print s.find('bra', 2)

# str.lower()
print s.islower()

# str.split()
print s.split('ca')

# Exercise 8
print '\nExercise 8\n'

w = 'annapolis'
s = 'radar'
print s == s[::-1]

# Exercise 9
print '\nExercise 9\n'

# Exercise 10
print '\nExercise 10\n'


def rotate_word(string, int):
    crypt = []
    for i in string:
        c = ord(i) + int
        crypt.append(chr(c))
    print ''.join(crypt)


rotate_word('cheer', 7)
