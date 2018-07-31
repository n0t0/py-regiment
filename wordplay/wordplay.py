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
    for letter in required_letters:
        if letter in word:
            print 'ok'
        else:
            print 'letters:', required_letters, 'not found in word:', word

uses_only('dp', 'sa')


# exercise 5


def uses_all(word_list, required_letters):
    
    for word in word_list:
        if required_letters in word:
            print word


uses_all(word_list, 'brother')

def uses_all_impr(word_list, required):
    return uses_only(word, required)
uses_all_impr(word_list, 'bro')
    

# exercise 6


def is_abecedarian(word_list):
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c 
    return True


def is_abecedarian_im(word):
    i = 0 
    while i < len(word) - 1:
        if word[i + 1] < word[i]:
            return False
        i = i + 1 
    return True

is_abecedarian_im(word)


    
    
    
