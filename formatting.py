####Basic Formatting####
########################

# OLD METHOD; order of arguments doesn't change

s = "Sralo %s na pateche. Koi go qde? - %s" % ('meche', 'Ti')
print s

# NEW METHOD; index position allowing for order change

s = 'Sralo {} na pateche. Koi go qde? - {}'.format('meche', 'Ti')
print s
s = 'Sralo {1} na pateche. Koi go qde? - {0}'.format('meche', 'Ti')
print s

# Indexing order of arguments Ex.2

s2 = '%d, %d, %d, %d' % (1, 2, 3, 4)
print s2
s2 = '{}, {}, {}, {}'.format(1, 2, 3, 4)
print s2
s2 = '{3}, {2}, {1}, {0}'.format(1, 2, 3, 4)
print s2

# Indexing order of arguments Ex.3

location = 'San Diego'
year = 2022
print 'By {} I wanna be living in {}!'.format(year, location)
print 'Composed at {time} on {date}!'.format(time = '19:39', date = '07/30/2017')

####Alligning strings####
#########################

# OLD METHOD

s = "10 spaces to the right"
print '%10s spaces to the right' % ('10')
print '%-10s spaces to the left' % ('10')

# NEW METHOD - can specify a indenting characther; can also center align

print '{:_>10} spaces to the right'.format('10')
print '{:=<10} spaces to the left'.format('10')
print '{:^10} spaces to the left'.format('10')

####Digits/Numbers####
######################

print 'What is the answer of the Universe? - %d' % (42)
print 'What is the emergency phone number? - {:d}'.format(911)

# Indeting is also possible with Numbers

print '%10d' % (4) # OLD METHOD
print '{:20d}'.format(4) # NEW METHOD
print '%010d' % (4) # total 10 digits including the integer
print '{:05d}'.format(4)

####Formatting floating point number####
########################################

print '10 digits filled after Floating point number %.10f' % (12.2051242)
print '4 digits after Floating point number %.4f' % (8.4754089)
print '2 digits after Floating point number %.2f' % (2.1511)
print 'Floating point number %f' % (2.23) # filled with 6 by default
print 'Indent by 6 digits with 2 after decimal point %06.2f' % (2.2051) # total 6 characters
print 'Indent by 10 total with 4 after decimal point %010.4f' % (2.2051) # total 10 characters
print 'Indent by 10 total with 6 after decimal point %010.6f' % (2.2051) # total 10 characters
print 'Indent by 14 total with 3 after decimal point; no zeros %14.3f' % (2.2051)
print '{:06.2f}'.format(1.2) # NEW METHOD rounds up*
print '{:.2f}'.format(41.21532358972678935) # .2 rounds up
print '{:.5f}'.format(41.21532358972678935) # above .2 cuts after dicimal point

# Ex.2 using round() method

s = 2.5235235252
print round(s, 2)

# Positive and Negative Numbers

print '%+d' % (10) # positive
print '% d' % (10) # negative
print '{:+d}'.format(10)
print '{:=+10d}'.format(10) # NEW METHOD allows padding related to the sign

####Defined Placeholders####
############################

d = {'given': 'Mila', 'last': 'Varta'}
print '%(given)s %(last)s' % d
print '{given} {last}'.format(**d)
print '{x} {y} {z}'.format(x='Id', y='Ego', z='Superego') # NEW METHOD allows assigning

# Accessing nested data structures NEW METHOD - Ex.2
# NEW METHODS supports __getitem__ for dictionaries and lists

customer = {'first': 'Happy', 'last': 'Customer'}
print '{c[first]} {c[last]}'.format(c=customer)

digits = [10,20,33,40,50]
print '{d[2]}{d[0]}'.format(d=digits)

# Also getattr() on objects

class Car(object):
    type = 'Sedan'
print '{c.type}'.format(c=Car)

# Both type of access can be freely mixed

class Car(object):
    type = 'SUV'
    make = [{'Lada': 'Niva'}, {'Jeep': 'Wrangler'}]
print '{c.type} {c.make[0][Lada]}'.format(c=Car)

####Parameters####
##################

# Parameters are nested expressions after : in the parent {} format

print '{:{align}{indent}}'.format('title', align='^', indent='10').upper()

# Precision

print '%.*s = %.*f' % (3, 'NOKIA', 3, 64.3248) # OLD METHOD
print '{:.{prec}} = {:.{prec}f}'.format('ALCATEL', 25.4214, prec=3)

# Indent & Precision

print '%*.*f' % (10, 2, 2.141421)
print '{:{indent}.{prec}f}'.format(3.23523, indent=5, prec=2)
