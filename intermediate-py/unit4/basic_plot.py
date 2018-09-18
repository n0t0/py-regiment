#%%
import matplotlib.pyplot as plt
import random


x_values = [0, 4, 7, 20, 22, 25]
y_values = [random.randint(0, 30) for i in x_values]
plt.plot(x_values, y_values, 'o-')
plt.ylabel('Values')
plt.xlabel('Time')
plt.title('Test plot')
plt.show()