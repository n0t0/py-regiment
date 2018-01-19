# Exercise 1

fin = open('z:/python/sowpods.txt', 'r').readlines() # no path needed if file is in same dir
# print fin.read()

wordlist = ['AbraFQW', ' whiteSpace ', '    tab ', ' punctua,tion!']

# for w in wordlist:
#     print w.lower().strip()
#     # print w.lower()

import string
print string.punctuation
print string.whitespace


def word_converter(fin):
    for word in fin:
        print word.lower().strip()
    # fin = [word.lower().strip() for word in fin]
word_converter(fin)
