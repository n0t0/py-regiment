# A String is a Sequence of Characters

car = 'mercedes'
letter = car[1] # indexing; computers count from 0
print letter
x = 2
print car[x+1] # variables, expressions and operators can be used for indexing

# len() Method (move to string_method.py)
print '===='*40

print len(car) # returns the number of characters in a string

lenght = len(car)
last = car[lenght-1]
print last

print car[-1] # negative indexing is allowed

# While and For Loops
print '===='*40

index = 0
while index < len(car):
    letter = car[index]
    print letter
    index += 1

for char in car:
    print char


# Indexing, Cutting & Slicing
print '===='*40

car = 'mercedes'

print car[:3] # cutting up to 3rd index
print car[3:] # cutting from 3rd index
print car[2:4] # slicing
print car[2:7:2] # cutting by 2
print len(car)
print car[:]


# Searching
print '===='*40

word = 'abracadabra'
def find(word, letter): # the opposite of [] operator; return an index number
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print find(word, 'c')

# Counting
print '===='*40

word = 'harmonica'
count = 0
for l in word:
    if l == 'a':
        count += 1
    print count

# The in Operator

print 'a' in 'harmonica'
print 'abc' in 'harmonica'

def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print letter


in_both('bravo', 'brava')
in_both('jaguar', 'tiger')
in_both('raspberry', 'orange')

# String Comparison

# NOTE: Relational operators work on strings

word = 'coco'
if word == 'raspberry':
    print 'so many berries'
