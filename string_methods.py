s = 'This is a string'
s2 = 'This is also a string'
s3 = 'ThIs sTrinG iS madE oF uPPer anD LoWER caSE chaRaCTeRS'

print s[:2]
print s2[::2]

print s.split()
print s2.splitlines()

for l in s3:
    if l.isupper() == True:
        print l

for c in s3:
    if c.isupper() == True:
        print c + ' BIGGIE'
    elif c.islower() == True:
        print c + ' smalls'
    else:
        print '|_|'
#print s3


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
