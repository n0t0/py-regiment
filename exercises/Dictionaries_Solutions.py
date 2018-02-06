print '\nExercise 1\n'
# Exercise 1
# Write a function that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn't matter what the values are. Then you can use the
# "in" operator as a fast way to check whether a string is in the dictionary.

# If you did Exercise 11, you can compare the speed of this implementation with
# the list in operator and the bisection search.

fin = open('z:/python/words.txt')


def words_keys(fin):
    # d = {}
    for word in fin:
        d = {key: None for key in fin}
        # NOTE: Test time() on dict and list
        # for i in d:
        #     print i
        # NOTE: Fix escape \n in words.txt
        print 'prodigal\n' in d
words_keys(fin)

print '\nExercise 2\n'
# Exercise 2


def histogram(s):
    d = dict()
    # v = c in s
    d = {c: 1 for c in s}
    for c in d:
        print d.get(c)
    #
    # else:
    #     print d.get(c, 0)
    #     print c, d[c]
        # print d.get(c)
    # for c in s:
    #     d = {c: 1 for c in s}
        # d[c] = 1
        # print d.get(c)
    #     if c not in d:
    #         d[c] = 1
    #     else:
    #         d[c] += 1
    # return d.get('s')

print histogram('stttttrumma')


# h = histrogram('s')
# print h


# Exercise 3
h = {'v': 1, 'a': 2, 'r': 1, 'd': 1, 'a': 1, 'r': 2}


def print_hist(h):
    # l = []
    for e in h.keys():
        l = []
        l.append(e)
        l.sort()
        print l

print_hist(h)
