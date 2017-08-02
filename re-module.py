import re

p = re.compile('ab*')
print p

s = '01-test'
matchObj = re.match('[0-9].', s, flags=0)
if matchObj:
    print 'Match: ', matchObj.group()


s = 'This is a test'
matchObj = re.search('^this is a (.*)' , s, re.I|re.M)
if matchObj:
    print 'Match: ', matchObj.group()
    print 'Match: ', matchObj.group(1)
    # print 'Match: ', matchObj.group(2)
