### Exercise 1

Python provides a built-in function called _len_ that returns the length of a string,
so the value of _len('peter')_ is 5. Write a function named _right_justify_ that takes
a string named s as a parameter and prints the string with enough leading spaces so
that the last letter of the string is in column 70 of the display.

```
>>> right_justify('signature')

                                                                  signature
```                                                                 

### Exercise 2  
A function object is a value you can assign to a variable or pass as an argument. For example, _do_twice_ is a function that takes a function object as an argument and calls it twice:

```
def do_twice(f):
    f()
    f()
```

Here’s an example that uses _do_twice_ to call a function named _print_spam_ twice.

```
def print_spam():
    print 'spam'

do_twice(print_spam)
```

1. Type this example into a script and test it.
2. Modify _do_twice_ so that it takes two arguments, a function object and a value,
and calls the function twice, passing the value as an argument.
3. Write a more general version of _print_spam_, called _print_twice_, that takes a
string as a parameter and prints it twice.
4. Use the modified version of _do_twice_ to call _print_twice_ twice, passing **'spam'**
as an argument.
5. Define a new function called _do_four_ that takes a function object and a value
and calls the function four times, passing the value as a parameter. There should
be only two statements in the body of this function, not four.                                                                  

### Exercise 3
This exercise can be done using only the statements and other features we have learned so far.

1. Write a function that draws a grid like the following:

```
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
```

Hint: to print more than one value on a line, you can print a comma-separated sequence:

```
print '+', '-'
If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.

print '+',
print '-'
The output of these statements is '+ -'.

A print statement all by itself ends the current line and goes to the next line.
```


2. Write a function that draws a similar grid with four rows and four columns.
