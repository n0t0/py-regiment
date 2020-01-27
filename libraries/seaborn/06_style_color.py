#%%
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

plt.switch_backend('agg')

tips = sns.load_dataset('tips')


# sns.set_style('whitegrid')
# sns.countplot(x='sex',data=tips)
# sns.despine()

# plt.savefig('style_01')

# plt.figure(figsize=(12,3))
# sns.set_context('poster')
# sns.countplot(x='sex',data=tips)

# plt.savefig('style_02')

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',palette='seismic')

# plt.savefig('style_03')
plt.show()

