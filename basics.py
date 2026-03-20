import pandas as pd
import numpy as np

data = {
    'name': ['Arjun', 'Bhavya', 'Chetan', 'Diya', 'Eshan'],
    'age': [23, 19, 34, 28, 22],
    'city': ['Hyd', 'Blr', 'Mum', 'Del', 'Pune'],
    'score': [78, 92, 65, 88, 71]
}

df = pd.DataFrame(data)
result=(
    df[['name','city','score']].loc[lambda x: x['score']>75]
           .sort_values(by='score',ascending=False)
           .reset_index(drop=True))
print(result)