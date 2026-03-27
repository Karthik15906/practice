'''
filtering in series, it basically means selecting only the data that matches certain conditions
'''


''' 1. basic filtering (condition based) '''
# conditions like >, <, == etc

import pandas as pd
s=pd.Series([10,20,30,40,50,60,70,80,90,100])
print(s[s>50])

# s>50 -> creates a boolean series, pandas keeps only true values



''' 2. multiple conditions '''
# we can combine conditions using &, |, ~

print(s[(s>20) & (s<50)])
# always use parenthesis with & and |



''' 3. filtering using isin() '''
# it used when checking multiple specific values

print(s.isin([10,40,80])) # this is boolean for every number like if 10 in series that index is true and others false

print(s[s.isin([10,40,80])])
# same like above only true values are printed
# it is useful for categorial filtering



''' 4. filtering using between() '''
# shortcut for range filtering insted of using condition

print(s.between(20,70)) # if it is in the range true else false

print(s[s.between(20,70)]) # prints true values


''' 5. filtering using where() '''
# where is one of most important 
# keeps all values but replaces non-matching ones with NaN
print(s.where(s>50))

# where() does not modify the original series by default to change the original series 
# we use inplace if inplace=True it changes the original series else false it does not changes
# by default it is false
# it is done like this s.where(s>50,inpalce=True) 


''' 6. filtering with mask() '''
# this is opposite of where() keeps non-matching ones but remaining are replaced with NaN
print(s.mask(s>50))


''' 7. filtering strings(inportant) '''
string=pd.Series(['apple','banana','cherry','date'])
print(string.str.contains('a')) # if a exsist in the string the true else false

# what actually happening in the statement:
# a pandas series is a colletion of values, not a single value because contains() is a
# string method, not a series method string.contains('a') X does not work
# to solve this we use .str this apply string operation to every element in the series
# to we use string.str.contains('a') same goes for startswith and endswith 
# can also use string.str.lower().str.contains() or string.str.upper().str.contains()
# remove unwanted values by s = s[~s.str.contains('a')]
# these are case-sensitive to make it insensitive we use case=False

# contains uses regex by default

print(string[string.str.contains('a',case=False)])
# startswith
print(string[string.str.startswith('a')])
# endswith
print(string[string.str.endswith('a')])

'''
    HANDING NAN (VERY IMPORTANT)
    if series has null values
'''
string1=pd.Series(['apple',None,'banana'])
print(string1.str.contains('a'))
# this gives none in result to fix it we do
print(string1.str.contains('a',na=False))

''' 8. using query()
    query() is not meant for series, it is designed for dataframes
    still, we can use it with series but rarely used
'''