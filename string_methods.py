s = 'This is a string'
s2 = 'This is also a string'
s3 = 'ThIs stRIng S madE oF UppEr aND LOwer caSE chaRactErS'

#### indexing, cutting & slicing a string
print '===='*40

print s[:2] # cutting
print s2[::2] # cutting 2 characters
print s2[5:12] # slicing
print len(s3)

#### split() | join()
print '===='*40

print s.split()
print s2.splitlines()


s4 = 'Abracadabra'
print s4.split('a')
print '--'.join(s4)

s5 = "Creating a LIST from a string"
print s5.split()
s6 = s5.split()
print s6
print '_____'.join(s6)

l = []
for word in s5.split():
    words = word.split()
    l.append(words)
print l

print '===='*40

# for w in s5:
#     print filter(lambda w: w.split(), s5.split())


print '===='*40

for w in s5.split():
    l = []
    l.append(w)
print l


#### isupper() | islower()
print '===='*40

l = []
for c in s3:
    if c.isupper() == True:
        l.append(c)
        print '--'.join(l)
# print '-'.join(l)

print '===='*40

for c in s3:
    if c.isupper() == True:
        print c + ' BIGGIE'
    elif c.islower() == True:
        print c + ' smalls'
    else:
        print '|_|'


def only_upper(s3):
    upper_case = ''
    for c in s3:
        if c.isupper() == True:
            upper_case += c
    return upper_case

print only_upper(s3)
print only_upper('PrintinG onlY UppeR CasE Chars')


def only_capital(s3):
    return filter(lambda x: x.isupper(), s3)

print only_capital(s3)
