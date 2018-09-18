#%%
import matplotlib.pylab as plt

data = open('z:/python/raw_data/life_span.txt', 'r').readlines()
# data = open('life_expectancies_usa.txt', 'r')

dates = []
male_life_expectancies = []
female_life_expectancies = []

for line in data:
    date, male_life_expectancy, female_life_expectancy = line.split(",")
    dates.append(date)
    male_life_expectancies.append(male_life_expectancy)
    female_life_expectancies.append(female_life_expectancy)


plt.plot(dates, male_life_expectancies, "bo-", label='Men')
plt.plot(dates, female_life_expectancies, "ro-", label='Women')

plt.legend(loc='upper left')
plt.xlabel('Age')
plt.ylabel('Year')
ply.title('Life expectancies for women and men in USA over time')
plt.show()
