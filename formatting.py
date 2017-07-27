####Basic Formatting####
########################

# OLD METHOD; order of arguments doesn't change

s = "Sralo %s na pateche. Koi go qde? - %s" % ('meche', 'Ti')
print s

# NEW METHOD; index positioning allowing for order change

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

print '10 digits after Floating point number %.10f' % (2.2051)
print '4 digits after Floating point number %.4f' % (2.2051)
print '2 digits after Floating point number %.2f' % (2.2051)
print 'Floating point number %f' % (2.2051) # 6 by default
print 'Indenting by 6 digits with 2 after decimal point %06.2f' % (2.2051) # total 6 characters
print 'Indent a Floating point number %010.4f' % (2.2051) # total 10 characters
print 'Indent a Floating point number %010.6f' % (2.2051) # total 10 characters

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
