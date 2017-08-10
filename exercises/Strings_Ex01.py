# Exercise 1
# Write a function that takes a string as an argument and displays the letters
# backward, one per line.

x = 'unforgiven'

def backward(x):
    for char in x[::-1]:
        print char

print backward(x)
