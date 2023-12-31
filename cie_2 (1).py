# -*- coding: utf-8 -*-
"""CIE---2

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gn-nw5RYlMDWoklotRQ9psTf2dRc8D55
"""

#perform EDA
import pandas as pd
df=pd.read_csv('/content/titanic.csv')
df.head()

df.describe()

df.info()

df.duplicated().sum()

df['Age'].unique()

df['Fare'].unique()

df.isnull().sum()

#Central tendency of Age and Fare
import pandas as pd
df=pd.read_csv('/content/titanic.csv')
#Central tendency of Age
age_mean=df['Age'].mean()
age_median=df['Age'].median()
age_mode=df['Age'].mode()[0]
print("mean of age:",age_mean)
print("median of age:",age_median)
print("mode of age:",age_mode)
print("----------------------------")
#Central tendency of Age
Fare_mean=df['Fare'].mean()
Fare_median=df['Fare'].median()
Fare_mode=df['Fare'].mode()[0]
print("mean of Fare:",Fare_mean)
print("median of Fare:",Fare_median)
print("mode of Fare:",Fare_mode)

import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('/content/titanic.csv')
df['Survived'].replace({0:'Not survived',1:'survived'}, inplace=True)
survived_counts=df['Survived'].value_counts()
sns.countplot(x='Survived',hue='Pclass',data=df)
plt.grid(2)
plt.show()
df.head(10)

df=pd.read_csv('/content/titanic.csv')
age_null=df['Age'].isnull().sum()
Fare_null=df['Fare'].isnull().sum()
df['Age'].fillna(df['Age'].mean(),inplace=True)
df['Fare'].fillna(df['Fare'].mean(),inplace=True)
age_after_mean=df['Age'].isnull().sum()
Fare_after_mean=df['Fare'].isnull().sum()
print("Age_null:",age_null)
print("Age_after_mean:",age_after_mean)
print("Fare_null:",Fare_null)
print("Fare after mean:",Fare_after_mean)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
df=pd.read_csv('/content/titanic.csv')
from scipy import stats
z_scores=np.abs(stats.zscore(df['Age']))
threshold=3
outliers=df['Age'][z_scores>threshold]
sns.boxplot(df["Age"],color='cyan')
plt.title('Boxplot of Fare column')
plt.xlabel('Age')
plt.show()

df.describe()

df.isnull().sum()