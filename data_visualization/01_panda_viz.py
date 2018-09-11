import numpy as np
import seaborn as sns
import pandas as pd 
import matplotlib.pyplot as plt
plt.switch_backend('agg')

df1 = pd.read_csv('df1',index_col=0)
df2 = pd.read_csv('df2')
df3 = pd.read_csv('df3')
# print(df1.head())


# df1['A'].hist(bins=30)
# plt.savefig('viz_01')

# df1['A'].plot(kind='hist',bins=30)
# plt.savefig('viz_01a')

# df2.plot.area(alpha=0.4)
# plt.savefig('viz_02a')

# df2.plot.bar(stacked=True)
# plt.savefig('viz_03a')
# plt.show()

# df1.plot.line(x=df1.index,y='B',figsize=(12,3),lw=1)
# plt.savefig('viz_04')

# df1.plot.scatter(x='A',y='B',s=df1['C']*100)
# plt.savefig('viz_05b')

# df2.plot.box()
# df = pd.DataFrame(np.random.randn(1000,2),columns=['a','b'])
# df.plot.hexbin(x='a',y='b',gridsize=25,cmap='coolwarm')
# plt.savefig('viz_06b')

df2['a'].plot.kde()
df2['a'].plot.denisty()
df2.plot.plot.denisty()