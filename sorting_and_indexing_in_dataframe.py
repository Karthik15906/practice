'''
Indexing (how to access data)
Sorting (how to arrange data)
'''
import pandas as pd

df = pd.DataFrame({
    'name': ['A', 'B', 'C'],
    'marks': [85, 92, 78]
}, index=['s1','s2','s3'])

'''Column Indexing (Basic)'''

print(df['name'])

# Multiple columns
print(df[['name', 'marks']])


'''.loc[] → label-based (MOST IMPORTANT)'''

print(df.loc['s1'])

# Multiple rows:
print(df.loc[['s1','s3']])
      
# Row + column:
print(df.loc['s1','marks'])

# multiple
print(df.loc[['s1','s2'],['name','marks']])



'''.iloc[] → position-based'''

print(df.iloc[0])        # first row
print(df.iloc[0, 1])     # first row, second column

# multiple

print(df.iloc[[0,2],[0,1]])

'''Fast Access: .at[] (label, single value), .iat[] (position, single value)'''

# .at[] (label, single value)
print(df.at['s1','marks'])

# .iat[] (position, single value)
print(df.iat[0,1])


'''Boolean Indexing (VERY IMPORTANT)'''

print(df[df['marks']>80])

# Multiple conditions
print(df[(df['marks']>80) & (df['name']=='A')])


'''Multiple conditions'''

print(df.loc['s1':'s2'])

print(df.iloc[0:2])


'''Fancy Indexing'''

print(df.loc[['s3','s1']])
print(df.iloc[[2,0]])


'''Setting Values (important)'''
df.loc['s1','marks']=90
print(df)


'''Sorting Techniques'''
'''Sort by Values (Column-wise)'''

print(df.sort_values(by='marks'))

# decending
print(df.sort_values(by='marks',ascending=False))


'''Multiple columns'''
print(df.sort_values(by=['marks','name']))


'''Sort by Index'''
# row index
print(df.sort_index())

# column index
print(df.sort_index(axis=1))


'''Handling Missing Values in Sorting'''
print(df.sort_values(by='marks',na_position='first'))


'''Reindex (VERY IMPORTANT)'''
# reorder rows
print(df.reindex(['s3','s1','s2']))

# add new row
print(df.reindex(['s1','s2','s3','s4']))
# s4 -> nan


'''Reset Index'''
# moves index into column
print(df.reset_index())


'''Set Index'''

print(df.set_index('name'))


'''Ranking in DataFrame
->It tells you the position of each value after sorting.
Step-by-step thinking
1. Sort values
20 → 1st  
30 → 2nd  
50 → 3rd  
2. Put ranks back in original order
50 → 3  
20 → 1  
30 → 2  
'''

print(df['marks'].rank(ascending=False))