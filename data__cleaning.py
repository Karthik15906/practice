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


'''
Data of Wrong Format
Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.

In our Data Frame, we have one cells with the wrong format Check out row 2 the 'join_date' column should be a string that represents a date
to convert all cells in the 'Date' column into dates.
Pandas has a to_datetime() method for this
'''

df['join_date']=pd.to_datetime(df['join_date'],errors='coerce')
print(df)
'''The errors='coerce' argument will replace any cells with wrong format with NaT (Not a Time) instead of throwing an error.
)

👉 it means:

“If Pandas cannot convert a value, don’t throw an error — just replace it with NaT (missing value).”
Think of it like this
Valid date → converted normally ✅
Invalid date → becomes NaT instead of crashing ❌➡️✔️
'''
# new_df=df.dropna()
new_df['join_date']=pd.to_datetime(new_df['join_date'],format='mixed',errors='coerce')
print(new_df)
'''format tells Pandas:

“This is the exact structure of my date string — parse it using this pattern.”

pd.to_datetime('15-01-2022', format='%d-%m-%Y')

👉 Pandas reads it like:

%d → day → 15
%m → month → 01
%Y → year → 2022

✅ Result: 2022-01-15

Why use format?
1. Faster parsing
If you specify format, Pandas doesn’t have to guess.

2. More strict (important)
If the format doesn’t match → it fails (or becomes NaT with coerce)
'''


''' Fixing Wrong Data
Wrong Data
"Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".

Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.

If you take a look at our data set, you can see that in row 6, the age is -5, which is not possible for an employee. So we can fix it by replacing it with a more reasonable value, like 25.
'''

'''Replacing Values
One way to fix wrong values is to replace them with something else.
'''
