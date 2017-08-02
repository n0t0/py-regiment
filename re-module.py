import re

# p = re.compile('ab*')
# print p

# match()

s = '01-test'
matchObj = re.match('[0-9].', s, flags=0)
if matchObj:
    print 'Match: ', matchObj.group()

s = 'This is a test'
matchObj = re.match('^this is (.) (.*)' , s, re.I|re.M)
if matchObj:
    print 'Matched: ', matchObj.group()
    print 'Matched: ', matchObj.group(1)
    print 'Matched: ', matchObj.group(2)

# search()

s = 'This is only a test'
search = re.search('only', s, re.I|re.M)
if search:
    print "Found: ", search.group()
    # print "Found: ", search.group(1)
    # print "Found: ", search.group(2)
    # print "Found: ", search.group(3)
