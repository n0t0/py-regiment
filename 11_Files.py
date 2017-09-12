# Writing a file

fout = open('output.txt', 'w')
print fout

line1 = 'This here is the wattle,\n'
fout.write(line1)
print fout

line2 = 'the emblem of our land.\n'
fout.write(line2)

# fout.close()

# The argument of write() has to be a string. Anything else needs to be converted

# Formatting

x  = 59
fout.write(str(x))

# option 2 is to use % format operator - modulus

camels = 42
'%d' % camels
print 'I have spotted %d camels.' % camels

print 'In %d years I have spotted %g %s.' % (3, 0.1, 'camels')

# Filenames and Paths

import os

cwd = os.getcwd()
print cwd

print os.path.abspath('memo.txt') # absolute path
print os.path.exists('memo.txt') # checking if file exists
print os.path.isdir('memo.txt') # checking if is a dir
print os.path.isfile('output.txt') # checking if is a file

print os.listdir(cwd) # returns a list of files in the cwd

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            print path
        else:
            walk(path)

# Catching Exceptions

try:
    fin = open('bad_file')
    for line in fin:
        print line
    fin.close()
except:``
    print 'Something went wrong.'
