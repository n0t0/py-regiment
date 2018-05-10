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

# print h.keys()

def print_hist(h):
    for c in h:
        print c, h[c]
print_hist(h)


def print_hist(h):
    for k, v in sorted(h.items()):
        print k, v 
print_hist(h)


print '\nExercise 4\n'
# Exercise 4


d = {'b': 1, 'g': 1, 'z': 0, 'o': 1, 'z': 2}
print d

def reverse_lookup(d, v):
    l = []
    for k in d:
        if d[k] == v:
            l.append(k)
    return l
k = reverse_lookup(d, 1)
print k


print '\nExercise 5\n'
# Exercise 5


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
print invert_dict(d)


def invert_dict(d):
    inverse = dict()
    for k in d:
        v = d[k]
        if v not in inverse:
            inverse.setdefault(v, [k])
        else:
            inverse[v].append(k)
    return inverse
print invert_dict(d)
    


