# A STRING is a sequence of characters

car = 'mercedes'
letter = car[1] # computers count from 0
print letter
x = 2
print car[x+1] # variables and operators can be used

# len() method (move to string_method.py)

print len(car) # returns the number of characters in a string

lenght = len(car)
last = car[lenght-1]
print last


# for and while loops
print 'sssss'

index = 0
while index < len(car):
    letter = car[index]
    print letter
    index += 1


for char in car:
    print char
