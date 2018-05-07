print '\nExercise 1\n'

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


s = {'key':'value'}
def his(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
his(s)



def histogram(s):
    d = dict()
    # v = c in s
    d = {c: 1 for c in s}
    d.get
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

print '\nExercise 3\n'
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
