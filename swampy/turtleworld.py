from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob

# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)

# for elt in range(4):
#     fd(bob, 100)
#     lt(bob)

# exercise 1 

'''
def square(t):
    for elt in range(4):
        fd(t, 50)
        lt(t)        
square(bob)
'''

# exercise 2

'''
def square(t, l):
    for elt in range(4):
        fd(t, l)
        lt(t)
square(bob, 150)
'''

# exercise 3

# def polygon(t, l, n):
#     for elt in range(360/n):
#         fd(t, l)
#         lt(t, n)
# polygon(bob, 30, 70)

def polygon(t, lenght, n):
    angle = 360.0 / n 
    for elt in range(n):
        fd(t, lenght)
        lt(t, angle)
polygon(bob, lenght=30, n=7)

# exercise 4

# C =  2 * 3.14 * r
# A = 
# bob.delay = 0.01 

# def circle(t, r):
#     polygon(t, 2, 1)
# # circle(bob, 20)
        
# # exercise 5

# def arc(angle):
#     for angle in circle(bob, 5):
#         if angle
# arc(180)
    
wait_for_user()