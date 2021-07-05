Day 12
'''
Day 12: pandas data filtering

Tutorial:
#Example - Loading Data
df = pd.read_csv('avocado.csv')
df = df.drop(columns = ['Unnamed: 0'])
df.head()

#Step 1: Create filter
user_filter = df['AveragePrice'] >= 1.30

#Step 2: Feed the filter in original DataFrame and store in new variable
filtered_df = df[user_filter]

#Step 3: Display Variable
filtered_df

Comparators:
>  x > y  x is greater than y
>=  x >= y x is greater than or equal to y
<  x < y  x is less than y
<= x <= y x is less than or equal to y
!= x != y x is not equal to y
== x == y x is equal to y


Challenge:
Examining the numbers, Dot understands that the prices of both conventional and organic avocados rise and fall frequently.
No matter how they grow the avocados, they don't want to sell them for less than $2.

Looking at recent years, Dot needs you to help them find: in which year or years did both conventional and organic avocados
have had average prices above $2?
'''
import pandas as pd

df = pd.read_csv('avocado.csv', index_col=0)

#My sol
df.groupby(['year', 'type']).max()

#hint
#Step 1: Create filter
user_filter = df['AveragePrice'] >= 2.0
#Step 2: Feed the filter in original DataFrame and store in new variable
filtered_df = df[user_filter]
#Step 3: Display Variable
filtered_df
df[df['AveragePrice'] >= 2.0]
