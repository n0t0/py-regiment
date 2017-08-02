import re

# p = re.compile('ab*')
# print p

# match()

s = '01-test'
match = re.match('[0-9].', s, flags=0)
if match:
    print 'Match: ', match.group()

s = 'This is a test'
match= re.match('^this is (.) (.*)' , s, re.I|re.M)
if match:
    print 'Matched:\t', match.group()
    print 'Matched:\t', match.group(1)
    print 'Matched:\t', match.group(2)

# search()

s = 'This is only a test'
search = re.search('^this is (.*) (.) (.*)', s, re.I|re.M)
if search:
    print "Found:\t", search.group()
    print "Found:", search.group(1)
    print "Found: ", search.group(2)
    print "Found: ", search.group(3)

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
