# -*- coding: utf-8 -*-
"""numpy_pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B4Q74G6E81XlqmrHhE3vj937KRKfYXm3
"""

import numpy as np
import pandas as pd

#Exercise 1:

#Creating numpy array containing the numbers from 1 to 10.
array1 = np.arange(1, 11)

print('array containing numbers from 1 to 10 :=> \n',array1)

#Reshaping array into 2x5 matrix.
reshaped_array = array1.reshape(2, 5)

print("\n Reshaped array :=> \n", reshaped_array)

#Exercise 2:

#Array containing the numbers from 1 to 20.
array2 = np.arange(1, 21)
print('Array containing numbers from 1 to 20 :=> \n', array2)

#Extracting elements between 5th and 15th index.
extracted_elements = array2[5: 15]
print('\n Elements between 5th and 15th index :=> \n', extracted_elements)

#Exercise 3:

#Pandas series with the following data: {'apples': 3, 'bananas': 2, 'oranges': 1}
data = {'apples':3, 'bananas': 2, 'oranges': 1}
pd_series = pd.Series(data)
print('Pandas Series with following data: \n', pd_series)

#Adding new item to the series with key 'pears' and value 4.
pd_series['pears'] = 4

#Output after adding new item.
print('\n Output after adding a new item: \n', pd_series )

#Exercise 4:

#Creating DataFrame with following columns: name, age and gender.
data = [ {'name': 'Alice', 'age': 25, 'gender': 'Female'},
         {'name': 'Bob', 'age': 30, 'gender': 'Male'},
         {'name': 'Charlie', 'age': 35, 'gender': 'Male'},
         {'name': 'David', 'age': 22, 'gender': 'Male'},
         {'name': 'Emma', 'age': 28, 'gender': 'Female'},
         {'name': 'Fiona', 'age': 31, 'gender': 'Female'},
         {'name': 'George', 'age': 27, 'gender': 'Male'},
         {'name': 'Hannah', 'age': 24, 'gender': 'Female'},
         {'name': 'Ian', 'age': 33, 'gender': 'Male'},
         {'name': 'Julia', 'age': 29, 'gender': 'Female'} ]

df = pd.DataFrame(data)

print(df)

#Exercise 5:

#Adding new column to the dataframe named occupation.
occupations = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst',
               'Programmer', 'Manager', 'Analyst', 'Programmer']

df['occupation'] = occupations

print('After adding occupation to the DataFrame : \n', df)

#Exercise 6:

#Rows of the DataFrame where age is greater than or equal to 30.
df_age_filtered = df[df['age'] >= 30]

print("DataFrame where age is greater than or equal to 30:\n", df_age_filtered)

#Exercise 7:

#Convert this DataFrame to a csv file.
df.to_csv('file1.csv', index=False)

#Reading the csv file.
read_df = pd.read_csv('file1.csv')

#displaying the contents
print('Displaying contents: \n', read_df)

