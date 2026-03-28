# filtering_in_dataframe
# filtering means selecting rows (or columns) based on some conditions

'''Basic Column Selection (Not really filtering yet)'''
import pandas as pd
df=pd.read_csv('pandas-practice\\data_dataframe\\data1_dataframe.csv')

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

