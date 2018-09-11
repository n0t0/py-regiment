import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.switch_backend('agg')

sns.set_style('whitegrid')
titanic = sns.load_dataset('titanic')
# print(titanic.head())


# Exercise 1 

# sns.jointplot(x='fare',y='age',data=titanic)
# plt.savefig('ex_01')

# Exercise 2 
 
# sns.distplot(titanic['fare'],
#              color='orange',
#              kde=False)
# plt.savefig('ex_02')


# Exercise 3 

# sns.boxplot(x='class',y='age',data=titanic)
# plt.savefig('ex_03')

# Exercise 4 

# sns.swarmplot(x='class',y='age',data=titanic)
# plt.savefig('ex_04')

# Exercise 5 

# sns.countplot(x='sex',data=titanic)
# plt.savefig('ex_05')

# Exercise 6 

# tc = titanic.corr()
# sns.heatmap(tc)
# plt.savefig('ex_06')

# Exercise 6 

g = sns.FacetGrid(data=titanic,col='sex')
g.map(sns.distplot, 'age')

plt.savefig('ex_07')