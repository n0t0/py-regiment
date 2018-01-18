### Exercise 1  
Many of the built-in functions use variable-length argument tuples. For example, max and min can take any number of arguments:

```
>>> max(1,2,3)
3
```

But sum does not.

```
>>> sum(1,2,3)
TypeError: sum expected at most 2 arguments, got 3
```

Write a function called sumall that takes any number of arguments and returns their sum.

### Exercise 2  
In following example, ties are broken by comparing words, so words with the same length appear in reverse alphabetical order. For other applications you might want to break ties at random. Modify this example so that words with the same length appear in random order. Hint: see the random function in the random module.


```
def sort_by_length(words):
    t = []
    for word in words:
       t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
```
