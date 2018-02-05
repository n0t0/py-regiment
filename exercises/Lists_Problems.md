### Exercise 1  
Write a function called _nested_sum_ that takes a nested list of integers and add up the elements from all of the nested lists.

Sometimes you want to traverse one list while building another. For example, the following function takes a list of strings and returns a new list that contains capitalized strings:

```
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
```

_res_ is initialized with an empty list; each time through the loop, we append the next element. So res is another kind of accumulator.

An operation like _capitalize_all_ is sometimes called a **map** because it “maps” a function (in this case the method capitalize) onto each of the elements in a sequence.

### Exercise 2  
Use _capitalize_all_ to write a function named _capitalize_nested_ that takes a nested list of strings and returns a new nested list with all strings capitalized.

Another common operation is to select some of the elements from a list and return a sublist. For example, the following function takes a list of strings and returns a list that contains only the uppercase strings:

```
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
```
_isupper_ is a string method that returns True if the string contains only upper case letters.

An operation like only_upper is called a filter because it selects some of the elements and filters out the others.

Most common list operations can be expressed as a combination of map, filter and reduce. Because these operations are so common, Python provides language features to support them, including the built-in function map and an operator called a “list comprehension.”

### Exercise 3  
Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].

### Exercise 4  
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].

### Exercise 5  
Write a function called _chop_ that takes a list, modifies it by removing the first and last elements, and returns None.

### Exercise 6   
Write a function called _is_sorted_ that takes a list as a parameter and returns _True_ if the list is sorted in ascending order and _False_ otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.
For example, _is_sorted([1,2,2])_ should return _True_ and _is_sorted(['b','a'])_ should return _False_.

### Exercise 7  
Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called _is_anagram_ that takes two strings and returns _True_ if they are anagrams.

### Exercise 8  
The (so-called) Birthday Paradox:

Write a function called _has_duplicates_ that takes a list and returns _True_ if there is any element that appears more than once. It should not modify the original list.
If there are 23 students in your class, what are the chances that two of you have the same birthday? You can estimate this probability by generating random samples of 23 birthdays and checking for matches. Hint: you can generate random birthdays with the _randint_ function in the _random module_.
You can read about this problem at http://en.wikipedia.org/wiki/Birthday_paradox.

### Exercise 9  
Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original. Hint: they don’t have to be in the same order.

### Exercise 10  
Write a function that reads the file words.txt and builds a list with one element per word. Write two versions of this function, one using the append method and the other using the idiom t = t + [x]. Which one takes longer to run? Why?

Hint: use the time module to measure elapsed time. Solution: http://thinkpython.com/code/wordlist.py.

### Exercise 11  
To check whether a word is in the word list, you could use the in operator, but it would be slow because it searches through the words in order.

Because the words are in alphabetical order, we can speed things up with a bisection search (also known as binary search), which is similar to what you do when you look a word up in the dictionary. You start in the middle and check to see whether the word you are looking for comes before the word in the middle of the list. If so, then you search the first half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, it will take about 17 steps to find the word or conclude that it’s not there.

Write a function called bisect that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not.

Or you could read the documentation of the bisect module and use that! Solution: http://thinkpython.com/code/inlist.py.

### Exercise 12  
Two words are a “reverse pair” if each is the reverse of the other. Write a program that finds all the reverse pairs in the word list. Solution: http://thinkpython.com/code/reverse_pair.py.

### Exercise 13  
Two words “interlock” if taking alternating letters from each forms a new word. For example, “shoe” and “cold” interlock to form “schooled.” Solution: http://thinkpython.com/code/interlock.py. Credit: This exercise is inspired by an example at http://puzzlers.org.

Write a program that finds all pairs of words that interlock. Hint: don’t enumerate all pairs!
Can you find any words that are three-way interlocked; that is, every third letter forms a word, starting from the first, second or third?
