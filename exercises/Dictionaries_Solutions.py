# Exercise 1
# Write a function that reads the words in words.txt and stores them as keys in
# a dictionary. It doesn't matter what the values are. Then you can use the
# "in" operator as a fast way to check whether a string is in the dictionary.

# If you did Exercise 11, you can compare the speed of this implementation with
# the list in operator and the bisection search.

fin = open('z:/python/words.txt')


def words_keys(fin):
    d = {}
    for word in fin:
        d = {key: None for key in fin}
        for i in d:
            print i

words_keys(fin)
