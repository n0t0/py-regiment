import matplotlib.pyplot as plt
import string

data = open('./constitution.txt', 'r').read()

letter_counts = {}

for char in string.ascii_lowercase:
    letter_counts[char] = 0

for char in data:
    char = char.lower()
    if char in string.ascii_lowercase:
        letter_counts[char] += 1

frequencies = letter_counts.items()
labels = []
counts = []

for letter, count in sorted(frequencies):
    labels.append(letter)
    counts.append(count)

xlocations = range(len(frequencies))
width = 0.5

plt.xticks([elem + width/2 for elem in xlocations], labels)
plt.bar(xlocations, counts, width=width)
plt.xlabel("Letter")
plt.ylabel("Frequency")
plt.title("Letter frequencies in the US Constitution")
plt.show()
