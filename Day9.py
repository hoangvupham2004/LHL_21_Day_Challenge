'''
Fill out the missing values in the *monthly milk production* column with the median, and fill out the *number of cows* column using the ***ffill*** method.

After filling in the missing values with our new data, answer these questions for Dot, so they can figure out the value of having a cow year-round:
1. What is the average for monthly milk production?
2. What is the standard deviation for monthly milk production?
3. What is the average number of cows used?
'''

import pandas as pd
df = pd.read_csv('milk_2.csv')
print(df.head(3)) #Inputing the value 3 inside the brackets of the df.head() function allows us to
                  #override the default value of 5.
print('\n') #
print(df.shape)

#Q1
median = df['Monthly milk production: pounds per cow'].median(skipna=True)
print(median)
df['Monthly milk production: pounds per cow'] = df['Monthly milk production: pounds per cow'].fillna(median)
df['Number of Cows'] = df['Number of Cows'].fillna(method='ffill')
mean = df.mean()
print(mean)

#Q2
std = df.std()
print(std)
