import pandas as pd 

df = pd.read_csv('Salaries.csv')
print(df)

print('8'*80)
print(df.head().info())
print(df.info())


print('8'*80)
print (df['BasePay'].mean())

print('8'*80)
print (df['OvertimePay'].max())

print('8'*80)
# print (df['JobTitle'=="JOSEPH DRISCOLL"])
# byTitle = df.groupby('JobTitle')
# print(byTitle.describe()['JOSEPH DRISCOLL'])
print (df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle'])
print('8'*80)
print (df[df['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits'])


print('8'*80)

print (df[df['TotalPayBenefits'] == df['TotalPayBenefits'].max()]['EmployeeName'])

print (df.loc[df['TotalPayBenefits'].idxmax()])

print('8'*80)
print (df.loc[df['TotalPayBenefits'].argmin()])
print (df.loc[df['TotalPayBenefits'].idxmin()])

print('8'*80)

byYear = df.groupby('Year')
print (byYear.mean()['BasePay'])

print('8'*80)

print (df['JobTitle'].nunique())

print('8'*80)

print (sum(df[df['Year'] == 2013]['JobTitle'].value_counts() == 1))
# print (byYear['Year'] == 2013 )
# print (df['JobTitle'].value_counts() == 1)

def chief_string(title):
    if 'chief' in title.lower().split():
        return True
    else:
        return False

print(sum(df['JobTitle'].apply(lambda x: chief_string(x))))

print('8'*80)

# print (df['title_len'] = df['JobTitle'].apply(len))
# print (df[['TotalPayBenefits', 'title_len']].corr())