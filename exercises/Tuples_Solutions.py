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
import itertools
import string

#### Read a word list from a file 
filename = "words.txt"
wordlist = open(filename).readlines(10000)
wordlist = [word.lower().strip() for word in wordlist]
    
anagram = []
# for a, b in itertools.combinations(wordlist, 2):
    # if tuple(a) == tuple(b) and len(a) == len(b):
    # if tuple(a) == tuple(b):
        # anagram.append(a)
        # anagram.append(b)
        # print a, b



for word in wordlist:
    anagram.append(tuple(word))

# for tup in anagram:
#     # print sorted(tup)
#     if sorted(tup) in anagram:
#         print len(tup)

for tup in anagram:
    for i in tup:
        i = l
    # if sorted(tup) in anagram[:]:
    #     print tup
    # print sorted(tup)
    # if sorted(tup) in anagram:
    #     print len(tup)


# def check(anagram, tup):
#     anagram = anagram[:]
#     if tup in anagram:
#         anagram.remove(tup)
    
#     first_vals = [x[0] for x in anagram]

#     if tup[0] not in first_vals:
#         return True

#     min_val = min([min(x[1:]) for x in anagram])

#     if max(anagram[1:]) < min_val:
#         return False

#     return True


    # seen = ()
    # if tup in anagram:
    #     seen.append(tup)
#     print seen
    

# print anagram
print type(anagram)


        

####### filename.close()



print '\nExercise 5\n'
# Exercise 5

def func1():
    pass

print '\nExercise 6\n'
# Exercise 6

def func2():
    pass





