'''
What is Indexing in Series?
Series = values + index
'''
import pandas as pd

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

'''Label-based Indexing'''
print(s['a'])  # Output: 10
print(s['b'])  # Output: 20
print(s[['a', 'c']])  # Output: a    10#         c    30

'''Position-based Indexing'''
print(s.iloc[0])  # Output: 10
print(s.iloc[1])  # Output: 20
print(s.iloc[[0, 2]])  # Output: a    10#         c    30

'''Slicing'''
print(s['a':'b'])  # Output: a    10#         b    20

'''Multiple Selection'''
print(s[['a', 'c']])  # Output: a    10#         c    30

'''Boolean Indexing'''
print(s[s > 15])  # Output: b    20#         c    30

'''Advanced Indexing (VERY IMPORTANT)'''

'''.loc[] → Label-based'''
print(s.loc['a'])  # Output: 10
print(s.loc['a':'c'])  # Output: 20

'''.iloc[] → Position-based'''
print(s.iloc[0])  # Output: 10
print(s.iloc[0:2])  # Output: a    10#         b    20

'''.at[] → Fast single value (label)'''
print(s.at['a'])  # Output: 10

'''.iat[] → Fast single value (position)'''
print(s.iat[0])  # Output: 10




'''Sorting Techniques in Series
can use inplace=True to modify the original Series instead of creating a new one.
'''

'''Sort by Values

    s.sort_values()
'''
s = pd.Series([30, 10, 20], index=['a', 'b', 'c'])
print(s.sort_values())  # Output: a    10#         b    20#         c    30

'''Descending Sort'''
print(s.sort_values(ascending=False))  # Output: c    30#         b    20#         a    10

'''Sort by Index'''
print(s.sort_index())  # Output: a    30#         b    10#         c    20

'''Sorting with Missing Values'''
s = pd.Series([30, None, 20], index=['a', 'b', 'c'])
print(s.sort_values())  # Output: a    30.0#         c
print(s.sort_values(na_position='first'))  # Output: b     NaN#         a    30.0#         c    20.0

'''Ranking (Sorting Related)
    s.rank()
    rank( assigns a position (rank )) to each value based on it's size 
    Important: Rank is NOT Index
    Index → position in Series
    Rank → position after sorting values
    rank() tells you where each value stands compared to others.

'''
s = pd.Series([100, 200, 100])
print(s.rank())