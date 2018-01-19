# Exercise 1
The os module provides a function called walk that is similar to this one
but more versatile. Read the documentation and use it to print the names
of the files in a given directory and its subdirectories.


# Exercise 2
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file and
write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message, and exit.
