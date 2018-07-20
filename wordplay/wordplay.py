from __future__ import division

fin = open('Z:\python\words.txt')

# exercise 1
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word


# exercise 2 
word_list = open('Z:\python\words.txt').readlines()

# def has_no_e():
#     for line in fin:
#         word = line.strip()
#         if 'e' not in word:
#             print word
# has_no_e()


def has_no_e():
    has_no_e = []
    for word in word_list:
        if 'e' not in word:
            has_no_e.append(word)
    p = len(has_no_e) / len(word_list)
    print '{:.2f}'.format(p), '%'
has_no_e()

    
