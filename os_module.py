import os

cwd = os.getcwd()
print cwd

print os.path.abspath('memo.txt') # absolute path
print os.path.exists('memo.txt') # checking if file exists
print os.path.isdir('memo.txt') # checking if is a dir
print os.path.isfile('output.txt') # checking if is a file
print os.listdir(cwd) # returns a list of files in the cwd
