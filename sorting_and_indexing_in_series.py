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