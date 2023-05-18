import os

import pandas as pd

path = os.getcwd() + "\Titanic\\train.csv"
titanic_df = pd.read_csv(path)

# print(titanic_df.head(5))
# print(titanic_df.info())
# print(titanic_df.describe().T)

#print(titanic_df.isnull().sum())
#print(titanic_df['Cabin'].head(20))
#print(titanic_df['Age'].dtypes)


# Create a new column 'Person' in which every person under 16 is child.
titanic_df['Person'] = titanic_df.Sex
titanic_df.loc[titanic_df['Age'] < 16, 'Person'] = 'Child'
print(titanic_df.columns)


