import pandas as pd
#creating a series from list
lst=[1,2,3,4,5]
df1=pd.Series(lst)
'''
    output
    ------
    index values
    0       1
    1       2
    2       3
    3       4
    4       5
'''
print(df1)
#series with custom indexes
df1=pd.Series(lst,['a','b','c','d','e'])
'''
    output
    ------
    a    1
    b    2
    c    3
    d    4
    e    5
'''
print(df1)
#creating a series from dictionary
data = {'apple': 5, 'banana': 3, 'cherry': 8}
s = pd.Series(data)
print(s)
# apple     5
# banana    3
# cherry    8
# dtype: int64
#now for scaler
data1=pd.Series(100,index=['a','b','c'])
print(data1)

#to know size
print(df1.size,s.size)

#to know datatype of series
print(df1.dtype,s.dtype)

#to know shape (tuple of dimensions)
print(df1.shape,s.shape)

#accessing an elements by labels
print(df1['a'])

#accessing an elements by position
print(df1[0])

#slicing by labels
'''it includes the step when using label'''
print(df1['a':'c'])

#slicing by index
'''it does not include step when using index'''
print(df1[0:3])