# Importing modules

import math

print math.sqrt(4)
print help(math.pow)
print math.pow(2,4)

# Importing module as a alias

import time as t

print t.time()

# Importing specific function from a module allows calling its function only

from calendar import firstweekday

print firstweekday()
