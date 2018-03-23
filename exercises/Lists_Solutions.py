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


l = [2,4,6,3,2,1,2]

def is_sorted(l):
    for e in l:
        if e > 0:
            e = e[1]
        return True
    else:
        return False
print is_sorted(l)
