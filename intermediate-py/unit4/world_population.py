#%%
import matplotlib.pyplot as plt

# data = open('z:/python/raw_data/population.txt', 'r').readlines()
data = open('z:/python/raw_data/population.txt', 'r')
dates = []
populations = []

for point in data:
    date, population = point.split()
    dates.append(date)
    populations.append(population)

plt.plot(dates, populations, 'o-')
plt.ylabel('World population in millions')
plt.xlabel('Year')
plt.title('World population over time')
plt.show()