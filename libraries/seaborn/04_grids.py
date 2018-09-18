#%%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.switch_backend('agg')

iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')


# print(iris['species'].unique())

# sns.pairplot(iris)
# iris.head()

#### PairGrid

g = sns.PairGrid(iris)
# g.map(plt.scatter)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

plt.show()
# plt.savefig('grid_02')

#### FacetGrid

# g = sns.FacetGrid(data=tips,col='time',row='smoker')
# g.map(sns.distplot, 'total_bill')

# plt.savefig('grid_03')