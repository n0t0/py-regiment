from __future__ import division

fin = open('Z:\python\words.txt')

# exercise 1

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word


# exercise 2 


word_list = open('Z:\python\words.txt').readlines()
word_list = [word.lower().strip() for word in word_list]


def has_no_e():
    has_no_e = []
    for word in word_list:
        if 'e' not in word:
            has_no_e.append(word)
    p = len(has_no_e) / len(word_list)
    print '{:.2f}'.format(p), '%'

has_no_e()

    
# exercise 3


def avoids(w, s):
    for w in word_list:
        if s not in w:
            print w
# avoids(has_no_e(), raw_input('enter forbbiden letters: '))    

# exercise 4


def uses_only(word, required_letters):
    # l = []
    for l in required_letters:
        if l in word:
            print 'ok'
        else:
            print required_letters, 'not found in', word

uses_only('dp', 'sa')





