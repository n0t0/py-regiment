import matplotlib.pyplot as plt 
import numpy as np 

plt.switch_backend('agg')

x = np.linspace(0,5,11)
y = x ** 2 


fig = plt.figure()

ax = fig.add_axes([0,0,1,1])

# ax.plot(x,y,color='orange', lw=1, ls='--', marker='o', ms=20, 
#        markerfacecolor="yellow",
#        markeredgewidth=3,
#        markeredgecolor='green') # RGB Hex Code --> #FF8C00

ax.plot(x,y,color='purple',lw=2,ls='--')

# ax.set_xlim([0,1])
# ax.set_ylim([0,2])

# plt.savefig('fig24')


# Special Plot Types
# seaborn library
plt.scatter(x,y)

# plt.savefig('fig25')