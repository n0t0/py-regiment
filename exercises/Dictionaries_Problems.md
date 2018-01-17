### Exercise 1  
Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the _in_ operator as a fast way to check whether a string is in the dictionary.

If you did Exercise 11, you can compare the speed of this implementation with the list in operator and the bisection search.

### Exercise 2  
Dictionaries have a method called get that takes a key and a default value. If the key appears in the dictionary, get returns the corresponding value; otherwise it returns the default value. For example:

```
>>> h = histogram('a')
>>> print h
{'a': 1}
>>> h.get('a', 0)
1
>>> h.get('b', 0)
0
```
Use get to write histogram more concisely. You should be able to eliminate the if statement.

### Exercise 3  
Dictionaries have a method called keys that returns the keys of the dictionary, in no particular order, as a list.

Modify print_hist to print the keys and their values in alphabetical order.

```
def print_hist(h):
    for c in h:
        print c, h[c]

Here’s what the output looks like:

h = histogram('parrot')
print_hist(h)
a 1
p 1
r 2
t 1
o 1
```

### Exercise 4  
Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none.

```
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError
```