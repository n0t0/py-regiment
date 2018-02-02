### Exercise 1
Write a function that takes a string as an argument and displays the letters
backward, one per line.

### Exercise 2
Modify the program to fix this error.

In Roberts McCloskey's book 'Make Way for Ducklings', the names of the ducklings
are Jack, Kack, Lack, Mack, Nack, Ouack, Pack, and Quack. This loop outputs
these names in order:

```
prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    print letter + suffix
```

The output is:

- Jack
- Kack
- Lack
- Mack
- Nack
- Oack
- Pack
- Qack

Of course, that's not quite right because "Ouack" and "Quack" are misspelled.

### Exercise 3
Modify _find_ so that it has a third parameter, the index in word
where it should start looking.

```
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
```

### Exercise 4
Encapsulate this code in a function named count, and generalize
it so that it accepts the string and the letter as arguments.

```
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count
```

### Exercise 5
Rewrite _count_ function so that instead of traversing the string,
it uses the three-parameter version of _find_ from the previous section.

### Exercise 6
There is a string method called _count_ that is similar to the function
in the previous exercise. Read the documentation of this method and
write an invocation that counts the number of as in 'abracadabra'.

```
word = 'abracadabra'
print word.count('a')
```

### Exercise 7
Read the documentation of the string methods at
http://docs.python.org/2/library/stdtypes.html#string-methods.
You might want to experiment with some of them to make sure you understand
how they work. strip() and replace() are particularly useful.

#### replace()

```
word = 'abracadabra'
print word.replace('a','-')
print word.replace('a','-', 2) # 3th argument counts occurences to be replaced
```

#### strip()

```
w = 'Metallica - Unforgiven.mp4'
print w.strip('.mp4')
```

The documentation uses a syntax that might be confusing.
For example, in find(sub[, start[, end]]), the brackets indicate optional
arguments. So sub is required, but start is optional, and if you include
start, then end is optional.

### Exercise 8
A string slice can take a third index that specifies the “step size;” that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

```
>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'
```
A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.

Use this idiom to write a one-line version of _is_palindrome_ from _Math_Problems - Exercise 5_.

### Exercise 9
The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).

```
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
```

### Exercise 10  
ROT13 is a weak form of encryption that involves “rotating” each letter in a word by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.

Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount.

For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.

You might want to use the built-in functions ord, which converts a character to a numeric code, and chr, which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily offended, find and decode some of them. Solution: http://thinkpython.com/code/rotate.py.
