'''
a dataframe is a 2d labeled data structure with
rows->indexes
columns->names 
each column can have a different datatype
'''
import pandas as pd
#it is dictionary, with set of rows and colums as a matrix
data={
    'name':['a','b','c'],
    'age':[17,18,19],
    'marks':[85,90,95]
}
df=pd.DataFrame(data)
print(df)
'''output
   name  age  marks
0    a   17     85
1    b   18     90
2    c   19     95
'''

# from list of lists to dataframe
df2=pd.DataFrame([[1,2],[3,4]],columns=['a','b'])
print(df2)

# to get columns names
print(df.columns)

# to get values 
print(df.values)

# to det indexes i.e, rows
print(df.index)

# now accessing in a dataframe
# if we use this we get the name 
# 0    a
# 1    b
# 2    c
print(df['name'])

# now to select multiple rows we use something like this [['name', 'age']]
print(df[['name','age']])

# print(df['a':'c']) this statement like not works it works when the idexes is labeled as 
# a,b,c then only it will work to make it work we need set the index as shown below
df1=df.set_index('name')
print(df1['a':'c'])

# slicing can be done in a dataframe same like series
print(df[0:2])
# numpy like slicing does not work like df[:,0:2] however it can be done using iloc method

# let's use loc , remember loc includes the end index
print(df.loc[0:2])

# let's use iloc it is index based and it does not include end index
print(df.iloc[:,0:2])
print(df.iloc[0:2,0:3])

'''
Additional: 
we can also create dataframe by reading .csv (comma seperated values) file
what pandas does is 

read file -> parse text -> organize into rows and cloumns -> assign labels

a csv files is just plain text
first line -> column names
next each line -> one row of data
'''

df3=pd.read_csv('pandas-practice/data_dataframe/data1_dataframe.csv')
print(df3)

'''
we can also create dataframe by json (java script object notation) too 
unlike csv which is tabular, json is structured like dictionary/ lists
in json datatype is preserved and it is highy flexiable comapared to csv
json is heavily used in
-> API's 
-> web apps
-> ML pipelines
'''

df4=pd.read_json('pandas-practice/data_dataframe/data2_dataframe.json')
print(df4)

# nested json (common in API's)
# this API format will not directly give clean dataframe
# to handle this we use .json_normalize

df5=pd.read_json('pandas-practice/data_dataframe/data3_dataframe.json')
print(df5)
import json
with open('pandas-practice/data_dataframe/data3_dataframe.json') as f:
    data=json.load(f)
df5=pd.json_normalize(data['students'])
print(df5)