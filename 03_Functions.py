# Def for Define a function

def lyrics():
    print 'Go, tell Aunt Rhodie,'
    print 'go, tel Aunt Rhodie.'
    print 'Go, tell Aunt Rhodie, the'
    print 'goose is in her bed!'

print lyrics()

# Calling a functions inside another function

def variation():
    print lyrics()
    print 'Hurry, tell Aunt Rhodie, oh, plase'
    print 'hurry tell Aunt Rhodie.'
    print 'Hurry, tell Aunt Rhodie that the'
    print 'goose is in her bed. (Quack, quack!)'

print variation()

# Flow of execution

def first():
    print 'This is the 1st function'
    print fourth()

def second():
    print 'This is the 2nd function'

def third():
    print 'This is the 3rd function'
    print first()

def fourth():
    print 'This is the 4th function'
    print second()

print third()

# NOTE: Parameters vs. Arguments
# Inside a function arguments are assigned to variables called parameters

def repeat(x): # argument
    print x # parameter
    print x # parameter

print repeat('s')
print repeat(2)
y = 3
print repeat(y)

# Local variables and parameters

def cat_repeat(part1, part2):
    cat = part1 + part2
    print repeat(cat)

print cat_repeat(2, 2)

line1 = 'King of the land! King of the land!'
line2 = 'Beast of the jungle say he is so grand!'
print cat_repeat(line1, line2)
