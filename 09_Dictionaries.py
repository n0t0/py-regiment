# Dictionary is Orderless; key-value'

d = {'do':'C', 'mi':'E', 'sol':'G'}
print d

# Adding an Entry or Changing a Value of a Key

d['la'] = 'A'
d['do'] = 'C4'
print d

# Dictionary methods

print d.keys() # returns the keys
print d.values() # returns the values of the keys
print d.items() # returns both in (key, value) tuples

# Ex.2
print '-'*40

weekDays = dict()
weekDays = {'Tuesday': 'martes',
            'Wednesday': 'miercoles',
            'Thursday': 'jueves',
            'Friday': 'viernes',
            'Saturday': 'sabado',
            'Sunday': 'domingo'}
weekDays['Monday'] = 'lunes'
print weekDays['Sunday']
print len(weekDays)
vals = weekDays.values()
print 'sabado' in vals

# Reverse lookup

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

# Dictionaries and Lists

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)

    return inverse
