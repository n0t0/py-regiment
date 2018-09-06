import pandas as pd 
import numpy as np
import re


ecom = pd.read_csv('Ecommerce Purchases')
# print(ecom)

print(ecom.head())

print('8'*80)
print(ecom.info())
print('8'*80)
print(ecom['Purchase Price'].mean())
print('8'*80)
print(ecom['Purchase Price'].max())
print(ecom['Purchase Price'].min())
print('8'*80)
print(ecom[ecom['Language'] == 'en'].count())
print('8'*80)
print(ecom[ecom['Job'] == 'Lawyer'].count())
print('8'*80)
print(ecom['AM or PM'].value_counts())
print('8'*80)
print(ecom['Job'].value_counts().head())
print('8'*80)
print(ecom[ecom['Lot'] == '90 WT']['Purchase Price'])
print('8'*80)
print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])
print('8'*80)
print(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].count())
print('8'*80)

year = '10/25'

# match = re.match('([0-9])(.*)', s, flags=0)
# if match:
#     print 'Match: ', match.groups() # returns a tuple

# match = re.match('(\d{2}/25)', year, flags=0)
# if match:
#     print ('Match: ', match.group()) # returns a tuple

# # def exp(card):
    
# print (ecom[ecom['CC Exp Date'] == '01/25'].count())
# print (sum(ecom[ecom['CC Exp Date'] == '25']['JobTitle'].value_counts() == 1))





