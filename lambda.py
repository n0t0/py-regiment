l = [1,2,3,4]

print reduce((lambda x,y: x+y ), l)

n = map(lambda v : v * 5, l)

print n

print '='*40

x = [2, 3, 4, 5, 6]
y = []
for v in x :
    if v % 2 :
        y += [v * 5]
# assert x == [2, 3, 4, 5, 6]
# assert y == [15, 25]
print y

print '='*40

y = map(lambda v : v * 5, filter(lambda u : u % 2, x))

print y


## 7/12/2017

tups = [
    ('s1', 2),
    ('s2', 4),
    ('s3', 8)
    ]

i = None

for t in tups:
    if i:
        if t[1] > i[1]:
            i = t
    else:
        i = t

print i

# a, b = tups
# print a
# print tups[2][1]

print '='*40

# TODO: How to interate over tuples: t[0][1]?

for i in tups[2][1:]:
    print i

for i, a in tups:
    print i, ':', a

z = reduce(lambda i, a: i > a, tups)
print z

a = None
#z = map(lambda t: reduce(lambda a: t > a, tups), tups)
#print z

print '='*40

z = reduce(lambda t : t * 20, tups[0][1:])
print z

# z = map(lambda t: reduce(lambda a: t[1]>a[1], tups)  a : i > a, tups)

# i = None
# z = map(lambda t: t[1] > i[1], tups)
#
# print tups

#
# map(lambda t,i: t[1]>i[1], tup)
#
# print i

#
