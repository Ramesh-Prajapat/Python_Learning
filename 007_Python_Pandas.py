import pandas as pd


## Create dataframe using dictionary

# df = pd.DataFrame({'col1': ['foo', 'foo'], 'col2': [1, 2]})
# print(df)


## Create dataframe using list

# cols = ['a', 'b']
# idx = ['x', 'y', 'z']
# df = pd.DataFrame([[1, 2], [3, 4], [5, 6]], columns=cols, index=idx)
# #print(type(df)) # Output will be Dataframe
# #print(type(df.a)) # Output will be Series


## Series
"""
Pandas Series is a one-dimensional labeled array in the Python programming 
language. It is a fundamental data structure of the Pandas library, which 
is built on top of NumPy. A Pandas Series can contain any data type (integers, 
floats, strings, etc.) and is capable of handling missing data.

Each element in a Pandas Series has a label or index that is used to identify 
the element. The index can be set to any value, including non-unique values, 
and can also be set to be a datetime or time period. This means that a Pandas 
Series can be used to represent time-series data.

One way to create a Pandas Series is by passing a Python list or NumPy array 
to the Series() constructor. For example
"""
# data = [10, 20, 30, 40]
# s = pd.Series(data)
# print(s)


## read_csv()
"""
read_csv is a function in the pandas library for Python that allows you to 
read data from a CSV file and create a DataFrame object.
"""


## info()
"""
In Pandas, the info() method is used to get a concise summary of a DataFrame. 
It provides information about the DataFrame such as the number of rows, the 
number of columns, the data type of each column, and the number of non-null 
values in each column. Here's the syntax of the info method:

DataFrame.info(verbose=True, null_counts=False)

1 verbose: A boolean value indicating whether to print a detailed summary 
(including data type and memory usage) or not. By default, it's set to True.

2.null_counts: A boolean value indicating whether to show the count of non-null
values or not. By default, it's set to False
"""

df = pd.read_csv('HR-Employee-Attrition-All.csv')
#print(df.info()) # To check data type of every column


## select_dtypes()
"""
select_dtypes is a function in the pandas library for Python that allows you to 
select columns from a DataFrame based on their data type. 

select_dtypes has other optional parameters, such as exclude, which allows you 
to specify which data types to exclude, and include_object, which allows you to 
include object (string) columns in the selection. You can find more information 
about these parameters in the pandas documentation.
"""

cols = df.select_dtypes(['object'])
#print(cols)


## astype()
"""
In Pandas, the astype() method is used to cast a pandas object to a specified 
data type. It returns a new object with the specified data type.
"""

for i in cols.columns:
    df[i] = df[i].astype('category')

# print(df.info())


## describe()
"""
describe is a method in the pandas library for Python that 
computes various summary statistics for each numerical column 
in a DataFrame.

describe has optional parameters that allow you to customize 
which summary statistics are computed, such as percentiles to 
specify the percentiles to compute, and include and exclude to 
specify which columns to include or exclude from the computation. 
You can find more information about these parameters in the pandas 
documentation.
"""
"""
describe().T is a method chain in the pandas library for Python 
that transposes the summary statistics computed by the describe()
"""

#print(df.describe())
#print(df.describe().T)
#print(df.describe(include=['category']).T)


## value_counts()
"""
value_counts is a method in the pandas library for Python that 
returns a series containing counts of unique values in a DataFrame 
or a series.

value_counts has optional parameters that allow you to customize 
the behavior, such as normalize to compute the frequency of each 
unique value instead of the count, and sort to control whether the 
counts are sorted in ascending or descending order. You can find 
more information about these parameters in the pandas documentation.

value_counts can also be used on a DataFrame column to count the 
number of occurrences of each unique combination of values in the 
column. In this case, the resulting object is a Series with a 
hierarchical index
"""

# cols = df.select_dtypes(['category'])
# for i in cols.columns:
#     print(f"Unique values in {i} are :")
#     print(cols[i].value_counts())
#     print('*'*50)


## drop()
"""
drop is a method in the pandas library for Python that removes 
one or more rows or columns from a DataFrame.

drop has several optional parameters that allow you to customize 
the behavior, such as axis to specify whether to drop rows or 
columns, inplace to modify the DataFrame in place instead of 
returning a new DataFrame, and labels to specify the rows or 
columns to drop by label or integer index. You can find more 
information about these parameters in the pandas documentation.

Note that drop returns a new DataFrame or Series with the specified 
rows or columns removed and does not modify the original DataFrame 
or Series unless the inplace parameter is set to True.
"""

df.drop(columns=['Over18'], inplace=True)
#print(df.columns)

df.drop(columns=['EmployeeNumber', 'EmployeeCount', 'StandardHours'], axis =1 ,inplace=True)
stats = df.describe(include=['category']).T
#print(stats)


## groupby()
"""
groupby is a method in the pandas library for Python that allows you 
to group a DataFrame by one or more columns and perform operations on 
the resulting groups.

groupby can also be used with multiple columns to group the data by 
multiple factors, and with different aggregation functions to compute 
different statistics for each group. You can find more information 
about these features in the pandas documentation.

Note that groupby returns a new GroupBy object, which can be used to 
apply various aggregation functions to the grouped data.
"""

# print(df.groupby(['Attrition', 'BusinessTravel'])['MonthlyIncome'].mean())
# print(df.groupby(['BusinessTravel', 'Attrition'])['Attrition'].count())
# print(df.groupby(['Attrition', 'JobRole'])['Attrition'].count())

# print(df[(df['MonthlyIncome'] >= 5000) | (df['MonthlyIncome']<= 8000)]['Attrition'].value_counts())
# print(df[(df['MonthlyIncome'] >= 2000) & (df['MonthlyIncome']<= 5000)]['Attrition'].value_counts())
# #t = df[(df['MonthlyIncome'] >= 500) & (df['MonthlyIncome']<= 3000)]['Attrition'].value_counts()
# t = df[(df['MonthlyIncome'] >= 5000) & (df['MonthlyIncome']<= 30000)]['Attrition'].value_counts()
# print((t['Yes']/(t['Yes'] + t['No'])))


## isna()
"""
isna is a method in the pandas library for Python that returns a Boolean
mask indicating which values in a DataFrame or Series are missing or NaN 
(Not a Number). 

isna can also be used with the notna method to get a mask indicating which 
values are not missing or NaN. These masks can be used to select or filter 
the rows or columns in a DataFrame that contain missing or non-missing values. 
You can find more information about these methods in the pandas documentation.

Note that isna returns a new DataFrame or Series with a Boolean mask, and 
does not modify the original DataFrame or Series.
"""

#print(df.MonthlyIncome.isna().sum())


## isnull()
"""
isnull() is a method in the Pandas library for Python that is used to detect 
missing or null values in a DataFrame or a Series.

When applied to a DataFrame, the isnull() method returns a DataFrame of the 
same shape as the original, with boolean values indicating whether each element 
is missing or not. The returned DataFrame has the same index and column labels 
as the original DataFrame.

When applied to a Series, the isnull() method returns a boolean Series of the 
same length as the original, with boolean values indicating whether each element 
is missing or not.
"""
#print(df.isnull())

## df.MonthlyIncome.fillna(df['MonthlyIncome'].mean(), inplace=True)


## dropna()
"""
dropna() is a method in the Pandas library of Python that is used to remove 
missing or null values from a pandas DataFrame or Series object.

The dropna() method allows you to remove rows or columns with missing or 
null values based on your specified conditions. You can specify the axis 
along which to drop the null values (0 for rows and 1 for columns) and several 
parameters such as how, thresh, subset, inplace, and subset.
"""

# df.dropna()