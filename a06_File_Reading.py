# Reading a File

fin = open('z:/python/words.txt') # no path needed if file is in same dir
print fin

# r --> for reading
# w --> for writing

print fin.readline()

# readline() keeps track of the file so when called again reads the next line

print fin.readline()

line = fin.readline()
word = line.strip() # method strip() removes the white space
print word
print word

# File Object as Part of a Loop

for line in fin:
    word = line.strip()
    print word

# Write a program that reads words.txt and prints only the words with more than
# 20 characters (not counting whitespace).

def more_than(f):
    for word in f:
        if len(word) > 20:
            print word

more_than(fin)
