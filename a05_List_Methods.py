# List Methods

# append()

l = ['classical', 'rock', 'pop', 'techno']
print l
l.append('electronic') # appends to the end of the list
print l

# insert()

l.insert(3, 'hip-hop') # index BEFORE inserting item or string
print l
l.insert(6, 'jazz')
print l

# remove()

l.remove('electronic')
print l

# remove() removes only the first instance

l = ['do','re','mi','fa','sol','sol','ti','do']
l.remove('sol')
print l

# pop() indexed item is deleted; if not index given - removes last
l.pop()
print l
x = l.pop(2)
print x

# extend() extends a list by another list

l.extend(['na', 'la', 'ta'])
print l

# sort() arranges the elements of the list from low to high

mus_alphabet = ['a', 'g', 'f', 'd', 'c', 'b', 'e']
mus_alphabet.sort()
print mus_alphabet
