#%%
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import stats


# plt.switch_backend('agg')

tips = sns.load_dataset('tips')
# print(tips.head())

#### Bar Plot 
# sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.std)
# plt.savefig('sns_07a')

#### Count Plot 

# sns.countplot(x='sex', data=tips)

#### Box Plot

# sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker')

# plt.show()
# plt.savefig('sns_08a')

#### Violin Plot

sns.violinplot(x='day',y='total_bill',data=tips,hue='sex',split=True)
plt.show()
# plt.savefig('sns_09a')

#### Strip Plot 

# sns.stripplot(x='day',y='total_bill',data=tips, jitter=True, hue='sex')

# plt.savefig('sns_10a')

#### Swarm Plot 

# sns.violinplot(x='day',y='total_bill',data=tips)
# sns.swarmplot(x='day',y='total_bill',data=tips,color='black')

# plt.savefig('sns_11a')

#### Factor Plot 

# sns.factorplot(x='day',y='total_bill',data=tips, kind='bar')
# plt.show()


