# -*- coding: utf-8 -*-
"""Missing values.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hE-PCjjD5Jf3fz0i50sZV8i4lNlJFefO
"""

#handling missing values using imputation
#importing the libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loading the dataset to pandas dataframe
dataset=pd.read_csv('/content/Placement_Dataset.csv')

dataset.head()

dataset.shape

dataset.isnull().sum()

# above there are 67 null values in salary column
#analyse the distribution of data in the salary
fig,ax=plt.subplots(figsize=(5,5))
sns.distplot(dataset['salary'])
plt.show()

"""we cannot use mean values in the place og graph. it is skew-distribution so we use median,mode"""

#replace the missing values with median value
dataset['salary'].fillna(dataset['salary'].median(),inplace=True)

dataset.isnull().sum()

"""now null values in salaries become 0
above one is imputation technique.
"""

#dropping technique
#dropping all the rows which contains the missing values
salary_dataset=pd.read_csv('/content/Placement_Dataset.csv')

salary_dataset.shape

salary_dataset.isnull().sum()

salary_dataset=salary_dataset.dropna(how='any')

salary_dataset.isnull().sum()

