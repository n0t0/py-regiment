### Exercise 1  
Write a compare function that returns **1** if **x > y**, **0** if **x == y**, and **-1** if **x < y**.

### Exercise 2  
Use incremental development to write a function called _hypotenuse_ that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments. Record each stage of the development process as you go.

### Exercise 3  
Write a function _is_between(x, y, z)_ that returns _True_ if **x ≤ y ≤ z** or _False_ otherwise.

### Exercise 4  
The Ackermann function, A(m, n), is defined:

```
              n+1	if  m = 0
A(m, n) =     A(m−1, 1)	if  m > 0  and  n = 0
              A(m−1, A(m, n−1))	if  m > 0  and  n > 0

```

See http://en.wikipedia.org/wiki/Ackermann_function. Write a function named _ack_ that evaluates Ackermann’s function. Use your function to evaluate _ack(3, 4)_, which should be **125**. What happens for larger values of **m** and **n**?

### Exercise 5
A _palindrome_ is a word that is spelled the same backward and forward, like **civic** and **racecar**. Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome.

The following are functions that take a string argument and return the first, last, and middle letters:

```
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]
```


Type these functions into a file named palindrome.py and test them out. What happens if you call middle with a string with two letters? One letter? What about the empty string, which is written ' ' and contains no letters?
Write a function called _is_palindrome_ that takes a string argument and returns _True_ if it is a palindrome and _False_ otherwise. Remember that you can use the built-in function _len_ to check the length of a string.


### Exercise 6  
A number, **a**, is a power of **b** if it is divisible by **b** and **a/b** is a power of **b**. Write a function called _is_power_ that takes parameters **a** and **b** and returns _True_ if **a** is a power of **b**. Note: you will have to think about the base case.

### Exercise 7  
The greatest common divisor (GCD) of **a** and **b** is the largest number that divides both of them with no remainder.

One way to find the GCD of two numbers is based on the observation that if **r** is the remainder when a is divided by **b**, then **gcd(a, b) = gcd(b, r)**. As a base case, we can use **gcd(a, 0) = a**.

Write a function called _gcd()_ that takes parameters _a_ and _b_ and returns their greatest common divisor.

Credit: This exercise is based on an example from Abelson and Sussman’s Structure and Interpretation of Computer Programs.


### Exercise 8
The built-in function _eval()_ takes a string and evaluates it using the Python interpreter. For example:

```
>>> eval('1 + 2 * 3')
7
>>> import math
>>> eval('math.sqrt(5)')
2.2360679774997898
>>> eval('type(math.pi)')
<type 'float'>
```

Write a function called _eval_loop_ that iteratively prompts the user, takes the resulting input and evaluates it using _eval()_, and prints the result.

It should continue until the user enters **'done'**, and then return the value of the last expression it evaluated.
