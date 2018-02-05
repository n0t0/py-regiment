print '\n Exercise 1\n'
### Exercise 1
# Write a function called nested_sum that takes a nested list of integers and
# add up the elements from all of the nested lists.

# Sometimes you want to traverse one list while building another.
# For example, the following function takes a list of strings and returns
# a new list that contains capitalized strings:

# def capitalize_all(t):
#     res = []
#     for s in t:
#         res.append(s.capitalize())
#     return res


# res is initialized with an empty list; each time through the loop, we append
# the next element. So res is another kind of accumulator.

# An operation like _capitalize_all_ is sometimes called a map because it
# "maps" a function (in this case the method capitalize) onto each of the
# elements in a sequence.


t = [1, 2, [3, 4], 5, 6, [[7, 8], 9, 10]]


# print len(t)
print t[2]
print t[5]
print t[5][0]
# total = t.append(t[2])
# print t

# l = [1, 2, 3, 4, 5]
# x = l.pop(0)
# print x


def nested_sum(t):
    total = []
    # total.append(t[2])
    # total.append(t[5])
    # total.append(t[5][0])
    for nest in t:
        if nest == t[2]:
            total.append(nest)
        elif nest == t[5] and t[5][0]:
            total.append(nest)
    # x = total.pop(0)
    # print x
    # y = total.pop(0)
    # print y
            # s = ' '.join(map(str, total))
            # print s
    # while t:
    #     total.extend(t.pop(0))
    print total
    x = total[0] + total[1]
    print x
    y = x.pop(2)
    print x.extend(y)
    print x
    print sum(x)
nested_sum(t)


print '\n Exercise 2\n'
# Exercise 2


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


nested_t = ['string1', ['String2', 'string3'], 'string4',['string5']]


def capitalized_nested(nested_t):
    nested_tCap = []
    for e in nested_t:
        if e == type(str):
            print type(e)
        # print e.capitalize()
        # if s.isupper()
        #     nested_tCap.append(s)
    # return nested_tCap
print capitalized_nested(nested_t)


print '\n Exercise 3\n'
# Exercise 3


t = [1, 2, 3]

def cum_sum(t):
    new_t = []
    for e in t:
        if e == 0:
            return 0
        elif e == 1:
            return e + 1
        else:
            return cum_sum(t) + cum_sum(t+1)
        # e = e + t[1]
        # new_t.append(e)
    # return new_t

print cum_sum(t)


# Exercise 4
# Write a function called middle that takes a list and returns a new list that
# contains all but the first and last elements. So middle([1,2,3,4]) should
# return [2,3].
print '===='*40

t = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def middle(t):
    cut = t[1:-1]
    return cut

print middle(t)

# Exercise 5
print '===='*40

s = 'hubbabubba'
l = list(s)


def chop(l):
    mod_l = l[1:-1]
    print mod_l
print chop(l)


# Exercise 6
print '===='*40

l = [2,4,6,3,2,1,2]

def is_sorted(l):
    for e in l:
        if e > 0:
            e = e[1]
        return True
    else:
        return False
print is_sorted(l)
