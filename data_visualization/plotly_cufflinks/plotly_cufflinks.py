#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import cufflinks as cf
# plt.switch_backend('agg')


from plotly import __version__
# print(__version__)
from plotly.offline import download_plotlyjs, plot, iplot, init_notebook_mode


init_notebook_mode(connected=True)
cf.go_offline()

# DATA

# df = pd.DataFrame(np.random.randn(100, 4), columns='A B C D'.split())
# df2 = pd.DataFrame({'Category': ['A', 'B', 'C'], 'Values': [32,43,50]})

# df.plot()
# plt.savefig('cf_01')
# plt.show()

# df.iplot(kind='scatter', x='A', y='B', mode='markers', size=20)

# df.iplot(kind='bar', x='Category', y='Values')

# df.iplot(kind='box')

df3 = pd.DataFrame({'x': [1,2,3,4,5], 'y': [10,20,30,20,10], 'z': [500,400,300,200,100]})
# print(df3)

df3.iplot(kind='surface')

df.iplot(kind='bubble', x='A', y='B', size='C')

df.scatter_matrix()