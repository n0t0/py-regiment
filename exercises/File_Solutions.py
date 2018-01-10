# Exercise 1
# Write a program that reads words.txt and prints only the words with more than
# 20 characters (not counting whitespace).

fin = open('z:/python/words.txt') # no path needed if file is in same dir
print fin

def more_than(f):
    for word in f:
        if len(word) > 20:
            print word

more_than(fin)
