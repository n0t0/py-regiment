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

## 7/25/2017


s = 'SomE arE UppER sOMe Are LOWEr'

def only_upper(s):
    return filter(lambda x: x.isupper(), s)

print only_upper(s)

## 6/29/2018

f = lambda a, b : a + b 
print f(7, 8)


l = [4, 5, 6, 7]

f1 = map(lambda x : x ** 2, l)
print f1


def fahrenheit(t):
    return ( (float(9) / 5 * t ) + 32 )
def celsious(t):
    return ( float(5) / 9 * (t - 32) ) 
temp = (36.5, 37, 37.5, 39)   

F = map(fahrenheit, temp)
C = map(celsious, F)

Celsius = [39.2, 36.5, 37.2, 37.8]
Fahrenheit = map(lambda x : (float(9) / 5) * x + 32, Celsius)
print Fahrenheit

C = map(lambda x: (float(5) / 9) * (x-32), Fahrenheit)
print C


a = [4, 5, 6, 7]
b = [14, 17, 21, 17]
c = [0, -2, 4, 55]

print map(lambda x, y : x + y, a, b)
print map(lambda x, y, z : x + y + z, a, b, c)


fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = filter(lambda x : x % 2, fib)
print result

f2 = reduce(lambda x, y : x + y, fib)
print f2


# finding the maximum 

f3 = lambda a, b : a if (a > b) else b
print reduce(f, fib)

# the sum in the range 

print reduce(lambda x, y : x + y, range(1,101))



