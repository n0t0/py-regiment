# a String is a sequence of characters

car = 'mercedes'
letter = car[1] # computers count from 0
print letter
x = 2
print car[x+1] # variables and operators can be used

# len() method (move to string_method.py)

print len(car) # returns the number of characters in a string

lenght = len(car)
last = car[lenght-1]
print last


# while and for loops
print '===='*40

index = 0
while index < len(car):
    letter = car[index]
    print letter
    index += 1

for char in car:
    print char


# indexing, cutting & slicing
print '===='*40

car = 'mercedes'

print car[:2] # cutting
print car[3:] # cutting 2 characters
print car[2:4] # slicing
print len(car)
print car[:]


# searching

word = 'abracadabra'
def find(word, letter): # the opposite of [] operator; return an index number
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1

print find(word, 'c')

# counting
print '===='*40

word = 'harmonica'
count = 0
for l in word:
    if l == 'a':
        count += 1
    print count
