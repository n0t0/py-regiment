# Exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

x = 'unforgiven'

def backward(x):
    for char in x[::-1]:
        print char

print backward(x)

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

# Exercise 3
# Modify find so that it has a third parameter, the index in word
# where it should start looking.

def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# NOTE: where the index in the word should be start looking?

# Exercise 4
# Encapsulate this code in a function named count, and generalize
# it so that it accepts the string and the letter as arguments.

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count


string = 'Today is raining.'
letter = 'i'


def count(string, letter):
    count = 0
    for x in string:
        if x == letter:
            count += 1
            print count

print count(string, letter)
