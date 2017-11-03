# Exercise 2
# Assume that we execute the following assignment statements:
# width = 17
# height = 12.0
# delimiter = '.'
# For each of the following expressions, write the value of the expression
# and the type (of the value of the expression).
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
    """Plug in a letter from the above expressions"""

    print 'The value of the expression is: {}'.format(x)
    print 'And its type is:', type(x)

print check_val_type(b)

# Exercise 3
# Practice using the Python interpreter as a calculator:

# 3.1 The volume of a sphere with radius r is 4/3 pi r^3. What is the volume
# of a sphere with radius 5? Hint: 392.7 is wrong!

# 3.2 Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?

# 3.3 If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile),
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time
# do I get home for breakfast?

# 3.1
# formula: V = 4/3 * pi * r ** 3

r = 5
print 'Volume of the sphere:', 4 * (3.14) * (5**3) / 3

# 3.2

book = 24.95 * 0.60 # %100 - %40 = %60; convert to decimal --> 0.60
shipping = 1 * 3 + 59 * 0.75
print 'Book after the discount:', book
print 'Shipping of 60 books:', shipping
print 'Total:', book * 60 + shipping

# 3.3

easy_pace = 8 * 60 + 15                          # 8 min and 15 sec in seconds
normal_tempo = 7 * 60 + 12                       # 7 min and 12 sec in seconds
tempo = easy_pace * 2 + normal_tempo * 3         # both tempos in seconds for 5 miles
left_the_house = 3600 * 6 + (52 * 60)            # 6:52 am in seconds
back_for_breakfast = left_the_house + tempo      # in seconds
back_for_breakfast / 3600                        # 7.5 hours; (floar-division 7 is wrong)
left_the_house / 60                              # 6:52 am in minutes
back_for_breakfast / 60                          # 7.5 hours in minutes
run = (back_for_breakfast - left_the_house) / 60 # in minutes

print ( left_the_house / 60 + run ) / 60         # 7.5 = 7:30 am Breakfast time!
