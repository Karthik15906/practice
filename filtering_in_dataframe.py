# filtering_in_dataframe
# filtering means selecting rows (or columns) based on some conditions

'''Basic Column Selection (Not really filtering yet)'''
import pandas as pd
df=pd.read_csv('pandas-practice\\data_dataframe\\data1_dataframe.csv')

# this just selects a cloumn, not filtering rows
print(df['marks'])
print(df[['name','marks']])

'''Boolean Filtering (Core Concept)'''

print(df[df['marks']>50]) # df['marks']>50 -> give true/false