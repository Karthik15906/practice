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

'''
Replace Empty Values
Another way of dealing with empty cells is to insert a new value instead.

This way you do not have to delete entire rows just because of some empty cells.
'''