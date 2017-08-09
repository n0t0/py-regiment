# Exercise 2
# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# delimiter = '.'
# For each of the following expressions, write the value of the expression and the type (of the value of the expression).
# width/2
# width/2.0
# height/3
# 1 + 2 * 5
# delimiter * 5
# Use the Python interpreter to check your answers.


width = 17
height = 12.0
delimiter = '.'

a = width/2
b = width/2.0
c = height/3
d = 1 + 2 * 5
e = delimiter * 5

def check_val_type(x):
    print x
    print type(x)

print check_val_type(e)

# Exercise 3
# Practice using the Python interpreter as a calculator:
# 3.1 The volume of a sphere with radius r is 4/3 pi r3. What is the volume of a sphere with radius 5? Hint: 392.7 is wrong!
# 3.2 Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy
# and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
# 3.3 If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile)
# and 1 mile at easy pace again, what time do I get home for breakfast?

# 3.1
# formula: V = 4/3 * pi * r ** 3
r = 5
print 4/3 * 3.14 * 5**3

# 3.2
b = 24.95 * 0.60 # %100 - %40 = %60; convert to decimal --> 0.60
shipping = 3 + 59 * 0.75
print b * 60 + shipping

# 3.3

easy_pace = 8 * 60 + 15       # seconds
normal_tempo = 7 * 60 + 12    # seconds

print easy_pace
print normal_tempo
print easy_pace * 2 + normal_tempo * 3
print ( easy_pace * 2 + normal_tempo * 3 ) / 60.0   # minutes
