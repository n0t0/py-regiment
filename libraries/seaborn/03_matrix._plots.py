#%%
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from scipy import stats


plt.switch_backend('agg')

tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

# tc = tips.corr()
# sns.heatmap(tc,annot=True)

# plt.savefig('mtx_01a')

fp = flights.pivot_table(index='month',columns='year',values='passengers')
# sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)
# plt.savefig('mtx_02b')
plt.show()

sns.clustermap(fp,cmap='coolwarm',standard_scale=1)
<<<<<<< HEAD
# plt.savefig('mtx_03a')
=======
# plt.savefig('mtx_03a')
plt.show()
>>>>>>> 3c01533b68af47423f5354f36b77ab4c5174c97c
