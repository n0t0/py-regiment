print '\nExercise 1\n'
# Exercise 1

a = [1, 2, 3, 4, 5, 6]


def sumall(*args):
    print sum(args)


sumall(1, 2, 3, 5, 8, 13)


print '\nExercise 2\n'
# Exercise 2
import random
words = ['dog', 'monkey', 'fly', 'crocodile',
         'horse', 'rhino', 'zebra', 'goose', 'camel']


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
    words = ['dog', 'monkey', 'fly', 'crocodile',
             'horse', 'rhino', 'zebra', 'goose', 'camel']

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


def signature(s):
    """Returns the signature of this string, which is a string
    that contains all of the letters in order.
    """
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t


def anagrams_list(filename):
    """
    List all anagrams in a list of words.
    """
# Read a word list from a file
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
    return d


def anagrams_print(d):
    """
    Prints the anagram sets in d.
    """

    for v in d.values():
        if len(v) > 1:
            print len(v), v


def print_anagram_sets_in_order(d):
    """Prints the anagram sets in d in decreasing order of size.

    d: map from words to list of their anagrams
    """

    # make a list of (length, word pairs)
    t = []
    for v in d.values():
        if len(v) > 1:
            t.append((len(v), v))

    # sort in ascending order of length
    t.sort()

    # print the sorted list
    for x in t:
        print x


def filter_length(d, n):
    """Select only the words in d that have n letters.

    d: map from word to list of anagrams
    n: integer number of letters

    Returns: new map from word to list of anagrams
    """
    res = {}
    for word, anagrams in d.iteritems():
        if len(word) == n:
            res[word] = anagrams
    return res


if __name__ == '__main__':
    d = anagrams_list('words.txt')
    print_anagram_sets_in_order(d)

    eight_letters = filter_length(d, 8)
    print_anagram_sets_in_order(eight_letters)


print '\nExercise 5\n'
# Exercise 5


def func1():
    pass


print '\nExercise 6\n'
# Exercise 6


def func2(word):
    for i in word:

    pass
