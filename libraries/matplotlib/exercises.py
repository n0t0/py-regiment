import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import matplotlib as mpl
import numpy as np 

plt.switch_backend('agg')

x = np.arange(0,100)
y = x*2 
z = x**2

#plt.show()

# Exercise 1 

# fig = plt.figure()

# ax = fig.add_axes([0,0,1,1])
# ax.set_ylabel('y')
# ax.set_xlabel('x')
# ax.set_title('title')
# ax.plot(x,y)

# plt.savefig('ex_01')


# Exercise 2

# fig = plt.figure()

# ax1 = fig.add_axes([0,0,1,1])
# ax2 = fig.add_axes([0.2,0.5,0.2,0.2])

# ax1.plot(x,y)
# ax2.plot(x,y)

# plt.savefig('ex_02')

# Exercise 3

# fig = plt.figure()

# ax1 = fig.add_axes([0,0,1,1])
# ax2 = fig.add_axes([0.2,0.5,.4,.4])

# ax1.plot(x,z)
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')

# ax2.plot(x,y)
# ax2.set_title('zoom')
# ax2.set_ylabel('y')
# ax2.set_xlabel('x')
# ax2.set_xlim(xmax=22, xmin=20)
# ax2.set_ylim(ymax=50, ymin=30)

# ax2.set_x
# plt.savefig('ex_03b')

# Exercise 4 


fig,axes = plt.subplots(nrows=1, ncols=2, figsize=(12,2))

axes[0].plot(x,y, lw=3, color='blue')
axes[0].set_xlim(xmax=100, xmin=0)
axes[0].set_ylim(ymax=200, ymin=0)

axes[1].plot(x,z, lw=3, color='red', ls='--')
axes[1].set_xlim(xmax=100, xmin=0)
axes[1].set_ylim(ymax=10000, ymin=0)


plt.tight_layout()
plt.savefig('ex_04b')
# plt.show()