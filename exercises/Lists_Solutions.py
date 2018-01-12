### Exercise 1
# Write a function called nested_sum that takes a nested list of integers and
# add up the elements from all of the nested lists.

# Sometimes you want to traverse one list while building another.
# For example, the following function takes a list of strings and returns
# a new list that contains capitalized strings:

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


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
print '===='*40
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




print nested_sum(t)
