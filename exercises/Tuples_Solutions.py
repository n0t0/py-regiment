# Exercise 1
# Many of the built-in functions use variable-length argument tuples.
# For example, max and min can take any number of arguments:

# >>> max(1,2,3)
# 3

# But sum does not.

# >>> sum(1,2,3)
# TypeError: sum expected at most 2 arguments, got 3

# Write a function called sumall that takes any number of arguments
# and returns their sum.

a = [1,2,3,4,5,6]


def sumall(*args):
    print sum(args)
sumall(1,2,3,5,8,13)


# Exercise 2
import random
words = ['dog', 'monkey', 'fly', 'crocodile', 'horse']

def sort_by_random(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))

    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res

if __name__ == '__main__':
    words = ['dog', 'monkey', 'fly', 'crocodile', 'horse']

    t = sort_by_random(words)
    for x in t:
        print x


# NOTE: list first element in a tuple and assign random.random() to those elements
def sort_by_random(words):
    t = []
    for word in words:
        t.append((len(word), word))

    lt = []
    for x, word in t:
        print x
        lt.append(x)
    print lt

    dupes = [x for n, x in enumerate(lt) if x in lt[:n]]
    # dupes = random.random()
    print dupes

    if dupes in t:
        # dupes = random.random()
        print 'ss'
        # if x == dupes:
    # [t[i] for i in range(len(t)) if not i == t.index(t[i])]
    # print t[i]
    #
    # for i in range(len(t)):
    #     if not i == t.index(t[i]):
    #         print t[i]

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
print sort_by_random(words)

# Exercise 3
s = 'today is a good day because the dog doesn\'t bark'
# NOTE: fix: print repeated chars only once
def most_frequent(s):
    count = 0
    lt = []
    for l in s:
        # s.sort(reverse=True)
        print s.count(l), l
        lt.append((s.count(l), l))
        # lt.append(l)
    lt.sort(reverse=True)
    for elem in lt:
        print elem
most_frequent(s)
