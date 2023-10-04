# -*- coding: utf-8 -*-
"""CIE--1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/148qjlgaroJYDKBO4EqB_jrt5tmunUEsL
"""

#creating two series using pd.series() function
import pandas as pd
Series_A=pd.Series([1,2,3,4,5])
Series_B=pd.Series([2,4,6,8,10])
common_items=Series_A[Series_A.isin(Series_B)]
print(common_items)

import pandas as pd
import matplotlib.pyplot as plt
#Load the dataset
data=pd.read_csv('mtcars.csv')
print(data)

#1.Histogram to check the frequency istribution of the variable 'mpg'
plt.figure(figsize=(8,6))
plt.hist(data['mpg'],bins=10,edgecolor='k')
plt.title('Frequency distribution of mpg')
plt.xlabel('mpg')
plt.ylabel('Frequency')
plt.show()

#2.scatter plot to determine the relation between wt of the car and mpg
plt.figure(figsize=(8,6))
plt.scatter(data['wt'],data['mpg'],color='green',marker='*')
plt.title('Relation between wt and mpg')
plt.xlabel('weight(wt)')
plt.ylabel('mpg')
plt.show()

trans=data['am'].value_counts()
plt.figure(figsize=(8,6))
trans.plot(kind='bar',edgecolor='k',color='orange')
plt.title('Frequency distribution of transmission type of cars')
plt.xlabel('Transmision type')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()

plt.figure(figsize=(8,6))
plt.boxplot(data['mpg'],notch=False,patch_artist=True)
plt.title('Box plot of mpg')
plt.xlabel('mpg')
plt.grid=True
plt.show()