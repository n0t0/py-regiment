# Exercise 1
The os module provides a function called _walk_. Read the documentation and use
it to print the names of the files in a given directory and its subdirectories.


# Exercise 2
Write a function called _sed_ that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file and
write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message, and exit.

# Exercise 3
In a large collection of MP3 files, there may be more than one copy of the same song, stored in different directories or with different file names. The goal of this exercise is to search for duplicates.

Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
To recognize duplicates, you can use _md5sum_ to compute a “checksum” for each files. If two files have the same checksum, they probably have the same contents.
To double-check, you can use the Unix command _diff_.

# Exercise 4

```
def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print linecount('wc.py')
```

```
import wc

print wc
<module 'wc' from 'wc.py'>

wc.linecount('wc.py')

```

Programs that will be imported as modules often use the following idiom:

```
if __name__ == '__main__':
    print linecount('wc.py')
```

Type this example into a file named wc.py and run it as a script. Then run the Python interpreter and import wc. What is the value of __name__ when the module is being imported?

Warning: If you import a module that has already been imported, Python does nothing. It does not re-read the file, even if it has changed.

If you want to reload a module, you can use the built-in function reload, but it can be tricky, so the safest thing to do is restart the interpreter and then import the module again.

### Exercise 5
The urllib module provides methods for manipulating URLs and downloading information from the web. The following example downloads and prints a secret message from thinkpython.com:

```
import urllib

conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn:
    print line.strip()
```
Run this code and follow the instructions you see there
