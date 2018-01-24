lt = ["cherries", "oranges", "lemons"]
print lt[::-1]

d = {"Jessica": "cherries", "Tom": "oranges", "Kim": "lemons"}
print d['Jessica']
d["Jessica"] = "pomegranate"
print d["Jessica"]
print d

# name = "David"
# fruit = "grape"
# t = [(name, fruit)]
# print t
# d.update(t)


# find novel words in Shakespeare's sonnets
import time

my_words = [elt.strip() for elt in open('z:/python/sonnet_words.txt', 'r').readlines()]
word_list = [elt.strip() for elt in open('z:/python/sowpods.txt', 'r').readlines()]
word_dict = dict((elt, None) for elt in word_list)

counter = 0
start = time.time()

for word in my_words:
    if word not in word_dict:
        print word
        counter += 1

stop = time.time()

print 'Total new words: %d' % counter
print 'Total elapsed: %.1f seconds' % (stop - start)
