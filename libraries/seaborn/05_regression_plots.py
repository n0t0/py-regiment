#%%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.switch_backend('agg')

tips = sns.load_dataset('tips')


# sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],
#           scatter_kws={'s': 40})

# plt.savefig('regr_01b')


sns.lmplot(x='total_bill',y='tip',data=tips,col='day',hue='sex',
          aspect=0.6, size=8)
plt.show()
# plt.savefig('regr_02a')
