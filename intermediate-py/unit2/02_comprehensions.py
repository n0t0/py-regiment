my_list = ['a', 'b','c', 'd', 'e']
print my_list
print [elt*2 for elt in my_list]

squares = [elt**2 for elt in range(10)]
print squares

word_list = [elt.strip() for elt in open('z:/python/sowpods.txt', 'r').readlines()]
print [elt for elt in word_list if 'UU' in elt]

word = 'radar'
print [word for word in word_list if word == word[::-1]]
