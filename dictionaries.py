# dictionary is orderless; key-value'

d = {'do':'C', 'mi':'E', 'sol':'G'}
print d

# adding an entry or changing a value of a key

d['la'] = 'A'
d['do'] = 'C4'
print d

# dictionary methods

print d.keys() # returns the keys
print d.values() # returns the values of the keys
print d.items() # returns both in (key, value) tuples 
