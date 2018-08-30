# pip install sqlalchemy
# pip install lxml
# pip install html5lib
# pip install BeautifulSoup4

import numpy as np
import pandas as pd

df = pd.read_csv('example.csv')
print(df)

df.to_csv('my_output', index=False)

print(pd.read_csv('my_output'))

print(pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1'))

df.to_excel('Excel_Sample_02.xlsx', sheet_name='NewSheet')

data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
# print(data)
# print(type(data))
print(data[0].head())

from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

df.to_sql('my_table', engine)

sqldf = pd.read_sql('my_table',con=engine)
print(sqldf)