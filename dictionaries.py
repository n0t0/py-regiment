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
