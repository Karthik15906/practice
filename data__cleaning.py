'''
Data cleaning in Pandas is basically the process of taking messy, raw data and making it usable for analysis or machine learning. Real-world data is almost never clean, so this step is critical.
in short,
Data cleaning means fixing bad data in your data set.

Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates

Why Data Cleaning is Needed ?

Raw data can have:
Missing values
Duplicate rows
Wrong data types
Inconsistent formatting
Outliers or invalid values

->Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result.
'''

import pandas as pd
df = pd.read_csv('pandas-practice/data_dataframe/employee_data.csv')
# empty cell -> removing the row
new_df=df.dropna()
print(new_df)
# rows containing null values has been removed from the dataframe.

# drops columns with missing values
new_df=df.dropna(axis=1)        # drops columns with missing value
print(new_df)

'''
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.

The fillna() method allows us to replace empty cells with a value.
'''
new_df=df.fillna(0)
print(new_df)

'''
To replace Only For Specified Columns 
To only replace empty values for one column, specify the column name for the DataFrame.
'''
new_df=df.fillna({'city':'unknown','age':100})
print(new_df)

'''
Replace Using Mean, Median, or Mode
A common way to replace empty cells, is to calculate the mean, median or mode value of the column.

Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column.
Mean = the average value (the sum of all values divided by number of values).
Median = the value in the middle, after you have sorted all values ascending.
Mode = the value that appears most frequently.
'''
new_df=df.fillna({'age':df['age'].mean(),'salary':df['salary'].median()})
print(new_df)