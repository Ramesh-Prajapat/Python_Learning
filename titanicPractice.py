import pandas as pd

titanic_df = pd.read_csv("C:\\Users\\Ramesh\\OneDrive\\Desktop\\Practice With Boss\\Titanic\\train.csv")
# print(titanic_df)

#print(titanic_df.info())

# print(titanic_df.describe())
# print(titanic_df.describe().T)

# cols = titanic_df.select_dtypes(['object'])
# for i in cols.columns:
#     titanic_df[i] = titanic_df[i].astype('category')


#
# cols = titanic_df.select_dtypes(['category'])
# for i in cols.columns:
#
#     print(f"Unique values in {i} are :")
#     print(cols[i].value_counts())
#     print('*'*50)

# print(titanic_df.isnull().sum())

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#sns.set(style="ticks")
#plt.style.use("fivethirtyeight")

# Let's first check gender
# 'catplot()': Figure-level interface for drawing categorical plots onto a FacetGrid.
# sns.catplot(x='Sex', data=titanic_df, kind='count')
# plt.show()


#Now let separate the gender by classes passing 'Sex' to the 'hue' parameter
# sns.catplot(x='Pclass', data=titanic_df, hue='Sex', kind='count')
# plt.show()

# Create a new column 'Person' in which every person under 16 is child.
titanic_df['Person'] = titanic_df.Sex
titanic_df.loc[titanic_df['Age'] < 16, 'Person'] = 'Child'


##Checking the distribution
# print(f"Person categories : \n{titanic_df.Person.unique()}\n=================================")
# print(f"Distribution of person : \n{titanic_df.Person.value_counts()}\n=================================")
# print(f"Mean age : {titanic_df.Age.mean()}\n=================================")

# sns.catplot(x='Pclass', data=titanic_df, hue='Person', kind='count')
# plt.show()

deck = titanic_df['Cabin'].dropna()
print(deck)

# let's grab that letter for the deck level with a simple for loop

levels = []
for level in deck:
    levels.append(level[0])

cabin_df = pd.DataFrame(levels)
cabin_df.columns = ['Cabin']
cabin_df.sort_values(by='Cabin', inplace=True)
# sns.catplot(x='Cabin', data=cabin_df, kind='count', palette='winter_d')
# plt.show()

cabin_df = cabin_df[cabin_df.Cabin != 'T']
sns.catplot(x='Cabin', data=cabin_df, kind='count', palette='summer')
plt.show()