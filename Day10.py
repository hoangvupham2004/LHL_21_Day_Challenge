"""
Day 10: pandas data modification
Dot shakes hands with the farmer after finalizing the purchase of the most beautiful cow on the farm, who's name is Bessie. They bring Bessie over to their cabin and set her up on the front lawn. Dot stares into the eyes of their new four-legged friend, envisioning all the good times they might have. Eating grass. Standing. Sleeping. Staring blankly into the distance. What a life they could have together!
But, another thought is starting to bother Dot...they're just one person, and they're not sure how much milk they'd be able to drink. They like putting dairy in their coffee and cereal just as much as anyone else, but drinking a tall glass of milk on its own kinda grosses them out.
What are they gonna do with all this milk? Ah-ha - maybe they can sell it! But how profitable will that be?

Challenge

Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:

Total Milk Production
Total Revenue
How much revenue did the cow farm make in the year 2020?
"""
import pandas as pd

df = pd.read_csv('milk_32.csv')
df = df.drop(columns = ['Unnamed: 0'])

df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']
#df.head()
#sort values of the 'Month' and return the values of months in 2020
print(df[df['Month'].str.contains("20")])
#answer is weird but for what I have, it works
print(df[df['Month'].str.contains("20")].sum())
