import random

print 'your lucky number is'
print random.randint(1, 6)

import scrabble

# print all words containing "uu"
for word in scrabble.wordlist:
    if "uu" in word:
        print word

# print all letters that don't appear double in words
import string


for letter in string.ascii_lowercase:
    exists = False
    for word in scrabble.wordlist:
        if letter * 2 in word:
            exists = True
            break
    if not exists:
        print "There are no English words with a double " + letter

# print all words that conntain all volews
vowels = 'aeiou'


def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True


for word in scrabble.wordlist:
    if has_all_vowels(word):
        print word

# fine the longest palindrome in english
word = 'apple'
print word[0]
print word[-1]
print word[1] == word[-2]


for index in range(len(word)):
    print index

word = 'radar'
is_palindrome = True
for index in range(len(word)):
    if word[index] != word[-(index + 1)]:
        is_palindrome = False
print is_palindrome


longest = ""
for word in scrabble.wordlist:
    is_palindrome = True
    for index in range(len(word)):
        if word[index] != word[-(index + 1)]:
            is_palindrome = False
    if is_palindrome and len(word) > len(longest):
        longest = word
print longest


for word in scrabble.wordlist:
    if list(word) == list(reversed(word)) and len(word) > len(longest):
        longest = word
print longest

import string
print string.ascii_lowercase
string.ascii_lowercase[0:25:3]
word = 'rotavator'
print word == word[::-1]


for word in scrabble.wordlist:
    if word == word[::-1] and len(word) > len(longest):
        longest = word
print longest
