# Exercise 1
import string

# fin = open('z:/python/sowpods.txt', 'r').readlines() # no path needed if file is in same dir
# # print fin.read()
#
# wordlist = ['AbraFQW', ' whiteSpace ', '    tab ', ' punctua,tion!']
#
# # for w in wordlist:
# #     print w.lower().strip()
# #     # print w.lower()
#
# print string.punctuation
# print string.whitespace
#
#
# def word_converter(fin):
#     for word in fin:
#         print word.lower().strip()
#     # fin = [word.lower().strip() for word in fin]
# word_converter(fin)

# v2

fin = open('z:/python/wordlist.txt', 'r')
words = fin.read()


def reader(words):
    w = string.whitespace
    p = string.punctuation
    result = ""
    for char in words:
        char.translate(None, string.whitespace)
        if char not in p and w:
            # print char
            result += char
    for word in result.strip().split():
        print word.lower()
reader(words)
