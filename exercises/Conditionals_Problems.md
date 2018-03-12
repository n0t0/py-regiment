### Exercise 1
Fermat’s Last Theorem says that there are no positive integers **a**, **b**, and **c** such that: **a\*\*n + b\*\*n = c\*\*** for any values greater than **2**.

1. Proof that there are no positive numbers to satisfy:
```
a**n + b**n = c**n for n>2
```

2. Write a function that prompts the user to input values for **a**, **b**, **c** and **n**
converts them to integers, and uses _check_fermat_ to check wheter they violate
Fermat's theorem.

### Exercise 2
If you are given three sticks, you may or may not be able to arrange them
in a triangle. For example, if one of the sticks is **12 inches** long and
the other two are **one inch** long, it is clear that you will not be able
to get the short sticks to meet in the middle. For any three lengths,
there is a simple test to see if it is possible to form a triangle:

If any of the three lengths is greater than the sum of the other two,
then you cannot form a triangle. Otherwise, you can. (If the sum of two
lengths equals the third, they form what is called a "degemerate" triangle.)

1. Write a function named _is_triangle_ that takes three integers as arguments,
and that prints either "Yes" or "No," depending on whether you can or cannot
form a triangle from sticks with the given lengths.

2. Write a function that prompts the user to input three stick lengths, converts
them to integers, and uses _is_triangle_ to check whether sticks with the given
lengths can form a triangle.
