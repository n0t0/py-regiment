def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

# Exercise 4
# Modify find so that it has a third parameter, the index in word
# where it should start looking.
