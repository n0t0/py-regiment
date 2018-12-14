from __future__ import division

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


nested_t = ['string1', ['String2', 'string3'], 'string4', ['string5']]


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


l = [3, 4, 9, 7, 8]


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
    anagram1 = {}
    anagram2 = {}
    print "Compare: ", s1.upper(), s2.upper()

    for c in s1:
        if anagram1.has_key(c):
            anagram1[c] += 1
        else:
            anagram1[c] = 1

    for c in s2:
        if anagram2.has_key(c):
            anagram2[c] += 1
        else:
            anagram2[c] = 1

    if anagram1 == anagram2:
        for i in s1 and s2:
            print s1.replace(i, '_'), s2.replace(i, '_')

    else:
        print "One or more characters don't match"
        print 'or'
        print "One or more characters extra"
        for k, v in anagram1.items():
            if v > 1:
                print k, v


# is_anagram('alena fanela', 'fanela alena')
is_anagram(s1, s2)


print '\n Exercise 8\n'.upper()
# Exercise 8
import random
import datetime
# 366 number of birthdays (February 29 included)


# combine two functions
def serial_date_to_string(srl_no):
    new_date = datetime.datetime(
        1970, 1, 1, 0, 0) + datetime.timedelta(srl_no - 1)
    return new_date.strftime("%Y-%m-%d")


birthdays = []

for student in range(23):
    birthdays.append(random.randint(1, 366))

print birthdays


def has_duplicates(birthdays):
    seen = set()
    for e in birthdays:
        if e in seen:
            print 'Birthday paradox:', serial_date_to_string(e)
            break
        seen.add(e)
    else:
        print 'no birthday paradox'


has_duplicates(birthdays)

# print birthdays

# print len(birthdays) != len(set(birthdays))


print '\n Exercise 9\n'.upper()
# Exercise 9

l = [2, 3, 4, 2, 2, 2, 5, 6, 6, 6, 18]


def remove_duplicates(l):
    uniq = []
    seen = set()
    for e in l:
        if e in seen:
            uniq.append(e)
        seen.add(e)
    print uniq
    print list(seen)


remove_duplicates(l)


print '\n Exercise 10\n'.upper()
# Exercise 10

WORD_LIST = "words.txt"
wordlist = open(WORD_LIST).readlines()
wordlist = [word.lower().strip() for word in wordlist]


def word_list2():
    t = []
    # fin = open("Z:\python\w.txt")
    fin = open("words.txt")
    for line in fin:
        word = line.strip()
        t.append(word)
    return t


# def word_list3():
#     t = []
#     # fin = open("Z:\python\w.txt")
#     fin = open("words.txt")
#     for line in fin:
#         word = line.strip()
#         t = t + [word]
#     return t


import time

start_time = time.time()
t = wordlist
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

start_time = time.time()
t = word_list2()
elapsed_time = time.time() - start_time

print len(t)
print t[:10]
print elapsed_time, 'seconds'

# start_time = time.time()
# t = word_list3()
# elapsed_time = time.time() - start_time

# print len(t)
# print t[:10]
# print elapsed_time, 'seconds'


print '\n Exercise 11\n'.upper()
# Exercise 11

from bisect import bisect_left


def makeword_list():
    """Reads lines from a file and builds a list using append.

    returns: list of strings
    """
    word_list = []
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        wordlist.append(word)
    return wordlist


def in_bisect(sor_list, target_v):
    if len(wordlist) == 0:
        return False

    i = len(wordlist) // 2
    if wordlist[i] == word:
        return True

    if wordlist[i] > word:
        # search the first half
        return in_bisect(wordlist[:i], word)
    else:
        # search the second half
        return in_bisect(wordlist[i+1:], word)


if __name__ == '__main__':
    wordlist = makeword_list()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list', in_bisect(wordlist, word))

    # for word in ['aa', 'alien', 'allen', 'zymurgy']:
    #     print(word, 'in list', in_bisect_cheat(wordlist, word))


in_bisect(wordlist, 'c')


# print '\n Exercise 12\n'.upper()
# # Exercise 12


# def reverse_pair():
#     for word in wordlist:
#         if word == word[::-1]:
#             print word


# reverse_pair()


# print '\n Exercise 13\n'.upper()
# # Exercise 13


# def interlock():
#     print 'work'
#     pass
