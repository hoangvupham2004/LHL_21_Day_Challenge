'''
Challenge 14

Dot's neighbour said that he only likes wine from Stellenbosch, Bordeaux, and the Okanagan Valley, and that the
sulfates can't be that high. The problem is, Dot can't really afford to spend tons of money on the wine.
Dot's conditions for searching for wine are:
    Sulfates cannot be higher than 0.6.
    The price has to be less than $20.

Use the above conditions to filter the data for questions 2 and 3 below.

Questions:

1. Where is Stellenbosch, anyway? How many wines from Stellenbosch are there in the entire dataset?
2. After filtering with the 2 conditions, what is the average price of wine from the Bordeaux region?
3. After filtering with the 2 conditions, what is the least expensive wine that's of the highest quality from the Okanagan Valley?

Stretch Question:
What is the average price of wine from Stellenbosch, according to the entire unfiltered dataset?
Note: Check the dataset to see if there are missing values; if there are, fill in missing values with the mean.
'''
import pandas as pd
df = pd.read_csv('winequality-red_2.csv')
df = df.drop(columns = ['Unnamed: 0'])

#1
df[df['region'] == 'Stellenbosch'].info() #35 entries
#2if < 0.6 and <=20 --> 11.72, but for the "suggested method", 11.30
df[(df['sulphates'] <= 0.6) & (df['price'] < 20) & (df['region'] == 'Bordeaux')].mean()
#3 very bad way... it works, but bad
#also, if < 0.6 and <=20 --> 1017, but for the "suggested method", 1025
filtered_value = df[(df['sulphates'] <= 0.6) & (df['price'] < 20) & (df['region'] == 'Okanagan Valley')]
filtered_value['quality'].max() #highest quality returns with 6
filtered_value[df['quality'] == 6].sort_values(by=['price'], ascending=True)

#or

filtered_value = df[(df['sulphates'] <= 0.6) & (df['price'] < 20) & (df['region'] == 'Okanagan Valley')]
filtered_value.groupby(['quality', 'price']).head()
#/srv/conda/envs/notebook/lib/python3.7/site-packages/ipykernel_launcher.py:3: UserWarning: Boolean Series key will
#be reindexed to match DataFrame index.
#This is separate from the ipykernel package so we can avoid doing imports until

#When sorting multiple features where we want one feature in ascending order and another in descending order, we can feed a Boolean list to the ascending parameter of the sort_values() function.
#filtered_df.sort_values(by=['column_1_Ascending','column_2_Descendng', 'column_3_Ascending'], ascending = [True, False, True])
