import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

print(df['W'])
print(type(df['W']))
print(type(df))

print(df.W)
print(df[['W','Z']])

df['New Column'] = df['W'] + df['Y']
print(df)

print(df.drop('New Column', axis=1, inplace=True))
print(df)

print(df.drop('E'))

print(df.shape)

# Selecting Rows

print(df.loc['A'])
print(df.iloc[2])

print(df.loc['B','Y'])
print(df.loc[['A','B'],['W','Y']])

# Conditional Selection

# print(df > 0)
# booldf = df > 0
# print(df[booldf])

# print(df['W']>0)
# print(df[df['W']>0])

# print(df[df['Z']<0])

# resultdf = df[df['W']>0]
# print(resultdf['X'])

# print(df[df['W']>0]['X'])
# print(df[df['W']>0]['Y','X'])

# Multiple Conditions 
print('8' * 80)
print(df[(df['W']>0) & (df['Y']> 1)])
print(df[(df['W']>0) | (df['Y']> 1)])

# Reset Index 

print(df.reset_index())

# Setting an Index

newind = 'CA NY WY OR CO'.split()
df['States'] = newind
print(df)

print(df.set_index('States'))

# Index Levels
print('8' * 80)

outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G1'].loc[1])

df.index.names = ['Groups', 'Num']
print(df)

print(df.loc['G2'].loc[2]['B'])
print(df.loc['G1'].loc[1]['A'])

print(df.xs(1, level='Num'))