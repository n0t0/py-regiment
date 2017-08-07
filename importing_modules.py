import math

print math.sqrt(4)
print help(math.pow)
print math.pow(2,4)

# importing module as a alias

import time as t

print t.time()

# importing specific function from a module allowing calling the function only

from calendar import firstweekday

print firstweekday()
