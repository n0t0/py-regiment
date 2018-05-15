# Exercise 1 
# print '\nExercise 1\n'
# import os

# cwd = os.getcwd()

# print cwd

# Exercise 2
# Write a function called sed that takes as arguments a pattern string,
# a replacement string, and two filenames; it should read the first file
# and write the contents into the second file (creating it if necessary).
# If the pattern string appears anywhere in the file, it should be replaced
# with the replacement string.

# If an error occurs while opening, reading, writing or closing files,
# your program should catch the exception, print an error message, and exit.
print '\nExercise 2\n'

import os

cwd = os.getcwd()
print cwd

f1 = open('Files_file1.txt', 'r')
print f1.read()

# def sed(string, r_string, f1, f2):
#     open('file1.txt')
#     open('file2.txt', 'w')
