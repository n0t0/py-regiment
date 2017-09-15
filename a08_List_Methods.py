# append() method

l = ['classical', 'rock', 'pop', 'techno']
print l
l.append('electronic') # appends to the end of the list
print l

# insert() method

l.insert(3, 'hip-hop') # index BEFORE inserting item or string
print l
l.insert(6, 'jazz')
print l

# remove() method

l.remove('electronic')
print l

# remove() removes only the first instance

l = ['do','re','mi','fa','sol','sol','ti','do']
l.remove('sol')
print l

# pop() indexed item is deleted; if not index given - removes last
l.pop()
print l
l.pop(2)
print l

# extend() extends a list by another list

l.extend(['na', 'la', 'ta'])
print l
