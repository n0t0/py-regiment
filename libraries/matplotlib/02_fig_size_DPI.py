import matplotlib.pyplot as plt 
import numpy as np 

plt.switch_backend('agg')

x = np.linspace(0,5,11)
y = x ** 2 

# fig = plt.figure(figsize=(8,2))

# ax = fig.add_axes([0,0,1,1])
# ax.plot(x,y)


# fig, axes = plt.subplots(nrows=2, ncols=1,figsize=(8,2))

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2,label='X Squared')
ax.plot(x,x**3,label='X Cubed')

ax.legend(loc=0)
# plt.tight_layout()
plt.savefig('fig18')
