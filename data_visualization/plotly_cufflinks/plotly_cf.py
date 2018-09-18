#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# from plotly import __version__
# from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

# import cufflinks as cf 
# init_notebook_mode(connected=True)

# cf.go_offline()

df = pd.DataFrame(np.random.randn(100,4), columns='A B C D'.split())
print(df.head())

df2 = pd.DataFrame({'Category': ['A','B','C'], 'Values': [32,43,50]})

df2.plot()
plt.show()