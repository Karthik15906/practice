# filtering_in_dataframe
# filtering means selecting rows (or columns) based on some conditions

'''Basic Column Selection (Not really filtering yet)'''
import pandas as pd
df=pd.read_csv('pandas-practice\\data_dataframe\\data1_dataframe.csv')

# The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())

# this just selects a cloumn, not filtering rows
print(df['marks'])
print(df[['name','marks']])

'''Boolean Filtering (Core Concept)'''

print(df[df['marks']>50]) # df['marks']>50 -> give true/false
# pandas keeps only true values

'''Multiple Conditions'''

# filtering based on multiple conditions

print(df[(df['marks']>50) & (df['marks']<90)])
print(df[(df['marks'] > 80) | (df['name'] == 'rahul')])
print(df[~(df['marks'] > 50)])

# Use &, |, ~ (not and, or, not)

'''Using .loc[] for Filtering'''

print(df.loc[df['marks']>50])
# same result but more flexible

# to select specific column 
print(df.loc[df['marks']>50,['name']])

'''Using .iloc[] (Index-based)'''

# df.iloc[rows, columns]

print(df.iloc[0:3])

# Slicing rows + Selecting columns,Slice both rows and columns
print(df.iloc[0:3,0:2])

# Slicing rows + Multiple columns
print(df.iloc[0:3,[0,2]])

# Single row + Slice columns
print(df.iloc[2,0:3])

# List of rows + Slice columns
print(df.iloc[[0,2,4],1:3])

'''df.iloc[rows, columns]'''

'''uery() Method (Very Clean Syntax)'''

print(df.query('marks >50'))
print(df.query("marks > 50 and marks < 90"))

# Looks like SQL → easier to read

'''isin() (Filter by Multiple Values)'''

print(df[df['name'].isin(['karthik','anu'])])
# Useful when checking multiple values

'''between() (Range Filtering)'''
# inclusive
print(df[df['marks'].between(50,90)])

'''String Filtering (str methods)'''

print(df[df['name'].str.contains('a')])
print(df[df['name'].str.startswith('a')])
print(df[df['name'].str.endswith('a')])

'''Null Filtering isna() / isnull()'''

print(df[df['marks'].isna()])
print(df[df['marks'].isnull()])
print(df[df['marks'].notna()])

'''Filtering with apply() (Advanced)'''

print(df[df['marks'].apply(lambda x :  x>50)])
# Slower, but useful for complex logic

'''Index-Based Filtering'''

print(df[df.index > 2])


'''Filtering Columns'''

print(df.filter(items=['name','marks']))
# with pattern
print(df.filter(like='ma'))