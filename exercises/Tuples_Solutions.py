print '\nExercise 1\n'
# Exercise 1 

a = [1,2,3,4,5,6]


def sumall(*args):
    print sum(args)
sumall(1,2,3,5,8,13)


print '\nExercise 2\n'
# Exercise 2
import random
words = ['dog', 'monkey', 'fly', 'crocodile', 'horse', 'rhino', 'zebra', 'goose', 'camel']


def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
print sort_by_length(words)


def sort_by_random(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)

    res = []
    for length, _, word in t:
        res.append(word)
    return res
print sort_by_random(words)

if __name__ == '__main__':
    words = ['dog', 'monkey', 'fly', 'crocodile', 'horse', 'rhino', 'zebra', 'goose', 'camel']

    t = sort_by_random(words)
    for x in t:
        print x


print '\nExercise 3\n'
# Exercise 3
s = 'today is a good day because the dog doesn\'t bark'
# TODO: fix: print repeated chars only once -- DONE
# TODO: replace first for loop with list comprehention -- DONE


def most_frequent(s):
    lt = [(s.count(l), l) for l in s]
    uniq = set(lt)
    for elem in sorted(uniq, reverse=True):
        print elem
most_frequent(s)

print '\nExercise 4\n'
# Exercise 4

WORD_LIST = "Z:\python\w.txt"
wordlist = open(WORD_LIST).readlines()
wordlist = [word.lower().strip() for word in wordlist]

my_words = [elt.strip() for elt in open('Z:\python\w.txt', 'r').readlines()]

# print my_words

import string
import time

set = string.ascii_lowercase
print set
d = {}


for l in set:
    d.setdefault(set, my_words) 
    d.setdefault(l, None) 
print d


def themuru():
    pass










