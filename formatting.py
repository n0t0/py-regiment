## BASIC FORMATTING

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

# Formatting floating point number

print 'Floating point number %.10f' % (2.2051)
print 'Floating point number %.4f' % (2.2051)
print 'Floating point number %.2f' % (2.2051)
print 'Floating point number %f' % (2.2051) # 6 by default

# Ex.2 using round()

s = 2.5235235252
print round(s, 2)

# Alligning strings

# OLD METHOD

s = "10 spaces to the right"
print '%10s spaces to the right' % ('10')
print '%-10s spaces to the left' % ('10')


# NEW METHOD - can specify a padding characther; can also center align 

print '{:_>10} spaces to the right'.format('10')
print '{:=<10} spaces to the left'.format('10')
print '{:^10} spaces to the left'.format('10')
