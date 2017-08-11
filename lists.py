# Just like a String, List is a sequence of values
# In a String, values are characters; in a List values are elements or items

# The elements of the list don't have to be from the same time

l = [40,50,60]
l2 = ['uno', 'dos', 'tres']
l3 = [2,3.0,'four',[5,6]] # a list within another list is nested
print l, l2, l3

# Unlike a Strings; Lists are mutable

wine = ['Merlot', 'Pinot Noir', 'Cabernet Souvignon', 'Malbec', 'Zinfandel']
print wine[2]

numbers = [20,30]
numbers[1] = 40
print numbers

# Traversing a List

for w in wine:
    print wine

for i in range(len(numbers)): # range() returns a List of indices
    print numbers[i] * 2

# List operations

a = [7,17,27]
b = [3, 13, 23]
c = a + b
print c

print [2] * 2
print [2, 12, 22] * 2

# List slices

scale = ['C','D','E','F','G','A','B','C']
print scale
print scale[2:5] # slice
print scale[:5]  # from beginning to index
print scale[3:]  # from index to end

# Since Lists are mutable, it is a good practice copy before operate them

scale[2] = ['Eb']
scale[5:7] = [['Ab','Bb']]
print scale
