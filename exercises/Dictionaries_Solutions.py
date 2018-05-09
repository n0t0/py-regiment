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


def his(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = his('a')
print h.get('a')
print h.get('b')


def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1 
    return d
print histogram('alabalanica')


print '\nExercise 3\n'
# Exercise 3
h = {'v': 1, 'a': 2, 'r': 1, 'd': 1, 'a': 1, 'r': 2}

print h.keys()

def print_hist(h):
    # l = []
    for e in h.keys():
        l = []
        l.append(e)
        l.sort()
        print l
print_hist(h)
