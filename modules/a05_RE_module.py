import re

# p = re.compile('ab*')
# print p

# match()
# match() is used with group(num=0) or groups() - returns a tuple

s = '01-test'
match = re.match('([0-9])(.*)', s, flags=0)
if match:
    print 'Match: ', match.groups() # returns a tuple

print type(match.groups())

s = 'This is a test'
match= re.match('^this is (.) (.*)' , s, re.I|re.M)
if match:
    print 'Matched:\t', match.group()
    print 'Matched:\t', match.group(1)
    print 'Matched:\t', match.group(2)

# search()
# search() is used with group(num=0) or groups() - returns a tuple

s = 'This is only a test'
search = re.search('^this is (.*) (.) (.*)', s, re.I|re.M)
if search:
    print "Found:\t", search.group()
    print "Found:", search.group(1)
    print "Found: ", search.group(2)
    print "Found: ", search.group(3)

if search:
    print 'Found:\t', search.groups() # returns a tuple

# match() Vs. search()
# match() - beginning of the string
# search() - anywhere in the string

s = 'Can you spot the difference?'
match = re.match('spot', s, re.I|re.M)
if match:
    print 'Matched: ', match.group()
else:
    print 'Sorry. No match!'

search = re.search('spot', s, re.I|re.M)
if search:
    print 'Found: ', search.group()
else:
    print 'Nothing found!'

# Search and Substitute

i = 'To find out more about X and Y go to Chapter #2 of the Book'

repl = re.sub('\#', 'No.', i) # \ cancels special character
print repl

repl = re.sub('\d', '3', i) # \d is the same as [0-9]
print repl

repl = re.sub('\D', '-', i) # \D is the same as [^0-9]
print repl

repl = re.sub(r'\s', '.', i) # \s matches whitespace character
print repl

repl = re.sub('[A-Z]', '!', i) # [A-Z] - upper only
print repl

repl = re.sub('X|Y', 'AB', i) # | either or
print repl

print dir(re)
