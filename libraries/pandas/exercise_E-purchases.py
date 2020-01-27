import pandas as pd 
import numpy as np
import re


ecom = pd.read_csv('Ecommerce Purchases')
print(ecom)

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
print(sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:] == '25' )))
print('8'*80)
print (ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head())







