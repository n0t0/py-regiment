import numpy as np
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
plt.switch_backend('agg')

df3 = pd.read_csv('df3')

# Exercise 1 

# df3.plot.scatter(x='a',y='b',
#                  figsize=(12,3),
#                  color='red',
#                  marker='o',
#                  markeredgewidth=2)
# plt.savefig('ex_01')

# Exercise 2 

# plt.style.use('ggplot')
# df3['a'].hist(color='orange',bins=30)
# plt.savefig('ex_02a')

# Exercise 3 

# df3['a','b'].plot.box()
# plt.savefig('ex_03')

# Exercise 4

# df3['d'].plot.kde(color='red',lw=1) 
# plt.savefig('ex_04')

# Exercise 5

# df3['d'].plot.kde(color='red',ls='--',lw=3) 
# plt.savefig('ex_05')

# Exercise 6

df3.plot.area(alpha=0.4).ix[[30]]
plt.savefig('ex_06')
