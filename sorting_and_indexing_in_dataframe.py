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