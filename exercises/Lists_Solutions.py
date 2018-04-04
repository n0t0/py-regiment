print '\n Exercise 1\n'.upper()
# Exercise 1

t = [1, 2, [3, 4], 5, 6, [[7, 8], 9, 10]]


def nested_sum(t):
    total = []
    for nest in t:
        if nest == t[2]:
            total.append(nest)
        elif nest == t[5] and t[5][0]:
            total.append(nest)
    print total
    x = total[0] + total[1]
    print x
    y = x.pop(2)
    print x.extend(y)
    print x
    print sum(x)
nested_sum(t)


print '\n Exercise 2\n'.upper()
# Exercise 2


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

nested_t = ['string1', ['String2', 'string3'], 'string4',['string5']]

def capitalized_nested(nested_t):
    nested_res = []
    for e in nested_t:
        print type(e)
        if type(e) == str:
            nested_res.append(e.capitalize())
        else:
            nested_res.append(capitalize_all(e))
    print nested_res
capitalized_nested(nested_t)


print '\n Exercise 3\n'.upper()
# Exercise 3


numbers = [1, 2, 3]


def cum(numbers):
    cumulative = []
    s = 0
    for x in numbers:
        s = s + x
        cumulative.append(s)
    print cumulative
cum(numbers)


print '\n Exercise 4\n'.upper()
# Exercise 4
# Write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements. So middle([1,2,3,4]) should
# return [2,3].


t = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def middle(t):
    cut = t[1:-1]
    return cut
print middle(t)

print '\n Exercise 5\n'.upper()
# Exercise 5

s = 'hubbabubba'
l = list(s)


def chop(l):
    mod_l = l[1:-1]
    print mod_l
print chop(l)

print '\n Exercise 6\n'.upper()
# Exercise 6


l = [3,4,9,7,8]


def is_sorted(l):
    for i, j in enumerate(l[:-1]):
        if j <= l[i+1]:
            print True, j
        else:
            return False, 'Not an ascending order list'
print is_sorted(l)


print '\n Exercise 7\n'.upper()
# Exercise 7

# version_01

s1 = 'listen'
print s1
s2 = 'silent'
print s2
print '\n'
ln = s2 

def is_anagram(s1, s2):
    for i in s1:
        if i in s2:
            s2 = s2.replace(i, ' ')
            print i.upper(), s2.upper()
        else:
            print False 
            print i, 'is already used in', ln
            break   
is_anagram(s1, s2)


print '\n Exercise 8\n'.upper()
# Exercise 8
import random

# print random.randint(0, 23)

### 366 number of birthdays (February 29 included)

birthdays = []

for student in range(23):
    # print random.randint(1,366)
    birthdays.append(random.randint(1,366))

print birthdays

# e = random.randint(1,366)

# def has_duplicates(birthdays):
#     for e in range(0, len(birthdays)):
#         for x in range(e + 1, len(birthdays)):
#             if birthdays[e] == birthdays[x]:
#                 print 'two people have birthdays on', e, x 
#     else:
#         print 'nobody matches someone\'s birthday'
# has_duplicates(birthdays)

def has_duplicates(birthdays):
    seen = set()
    for e in birthdays:
        if e in seen:
            print e, 'birthday paradox'
            break
        seen.add(e)
    else: 
        print 'no birthday paradox'
has_duplicates(birthdays)

print birthdays

print len(birthdays) != len(set(birthdays))

l = [2, 3, 4, 2]

def has_duplicates(l):
    seen = set()
    for e in l:
        if e in seen:
            print e
        seen.add(e)
    print 'tral'
has_duplicates(l)


print '\n Exercise 9\n'.upper()
# Exercise 9


def remove_duplicates(l):
    uniq = []
    seen = set()
    for e in l:
        if e in seen:
            uniq.append(e)
        seen.add(e)
    print uniq
remove_duplicates(l)



