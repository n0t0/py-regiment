import matplotlib.pyplot as plt 
import numpy as np 

plt.switch_backend('agg')

x = np.linspace(0,5,11)
y = x ** 2 

print(x)
print(y)

# functional method 

plt.plot(x, y)
#plt.show()
# plt.xlabel('X Label')
# plt.ylabel('Y Label')
# plt.title('Title')

# plt.subplot(1,2,1)
# plt.plot(x, y, 'r')
# plt.subplot(1,2,2)
# plt.plot(y, x, 'b')


# plt.savefig('fig3')

# object oriented method 

# fig = plt.figure()
# axes = fig.add_axes([0.1,0.1,0.8,0.8])
# axes.plot(x,y)
# axes.set_xlabel('X Label')
# axes.set_ylabel('Y Label')
# axes.set_title('Title')
# plt.savefig('fig5')

# fig = plt.figure()
# axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
# axes2 = fig.add_axes([0.2,0.5,0.4,0.3])

# axes1.plot(x,y)
# axes1.set_title('Larger Plot ')
# axes2.plot(y,x)
# axes2.set_title('Smaller Plot ')

# plt.savefig('fig8')

fig,axes = plt.subplots(nrows=1, ncols=2)
# plt.tight_layout()
# for current_ax in axes:
#     current_ax.plot(x,y)

# indexing the axes 
axes[0].plot(x,y)
axes[0].set_title('First Plot')
axes[1].plot(y,x)
axes[1].set_title('Second Plot')
plt.tight_layout()

plt.savefig('fig14')

# axes.plot(x,y)