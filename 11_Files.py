# Writing a File

fout = open('output.txt', 'w')
print fout

line1 = 'This here is the wattle,\n'
fout.write(line1)
print fout

line2 = 'the emblem of our land.\n'
fout.write(line2)

# fout.close() # closeing the file after writing to it

# NOTE:
# the argument of write() has to be a string; anything else needs to be converted

# Formatting

x  = 59
# fout.write(str(x))

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


print '-'
def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)
walk(cwd)

# Catching Exceptions with try and except

try:
    fin = open('bad_file')
    for line in fin:
        print line
    fin.close()
except:
    print 'Something went wrong.'

# Databases

import anydbm # accepts only strings

db = anydbm.open('database.db', 'c') # create a database
db['photo.png'] = 'Photo of Aliso' # update database as a dictionary
print db['photo.png']

for key in db:
    print key

db.close() # closing the database as any other file

# Pickling

import pickle # translates object types into a string and the back to objects

t1 = [1, 2, 3]
s = pickle.dumps(t1) # dump an object into a string
print s # readable for pickle to interpret
t2 = pickle.loads(s) # loads a string into a object
print t2

# Pipes

cmd = 'ls -l'
fp = os.popen(cmd)

res = fp.read()

stat = fp.close()
print stat

# md5sum

filename = 'book.tex'
cmd ='md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print res

# Writing Modules

def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count and
print linecount('wc.py')


import wc
