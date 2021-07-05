'''
Day 11: pandas group by basics
Dot's dreams of being a cow farmer seem to have been short-lived. When Dot wakes up in the morning, Bessie's already gone. Maybe they should have let her sleep in the house with them, but they didn't think the landlord would've liked that. After searching for a few hours, Dot finds Bessie hanging out with some mean-looking cows by an abandoned barn a little while away. All the cows have heavy septum rings hanging from their noses, and Dot is too scared to bother them.
As they walk back home, Dot feels sad about abandoning their newly-discovered dream of being a farmer. They're so caught up in their grief that they walk right into a big, leafy tree! A weird fruit fell from the tree and smacked Dot right in the head.
Rubbing their bruise, Dot looks at the fruit that hit them, curious. An avocado! Their head begins to spin with images as they imagine their future as a wildly successful avocado farmer.

Tutorial
Within pandas, one of the most essential and useful functions for data analysis is the group by function.
Group by does one thing: it groups the dataset according to a categorical column or columns. However, the grouping function can't stand on its own. The user needs to apply a specific aggregate function to the dataset after using group by. Check the example below.
import pandas as pd
df = pd.read_csv('avocado.csv', index_col = 0)
df.groupby(['year']).sum()
In the above code, we grouped the dataset by the year column, then used the sum() aggregate function to see the sum total of the numerical columns for each year. However, it doesn't have to the the sum() function, we can easily use another aggregate function such as mean().

Below is a list of aggregate functions we can use on our group bys.
count() – Number of non-null observations
sum() – Sum of values
mean() – Mean of values
median() – Arithmetic median of values
min() – Minimum
max() – Maximum
mode() – Mode
std() – Standard deviation
var() – Variance
Try this line of code below and see what it does:
df.groupby(['year','type']).count()
Before you continue to the challenge, play around with the group by function a bit. You can read more on the function in this article.
To learn more about the various pandas functions, check out the user guide in the pandas documentation.
Why should I use the documentation?
On the job as a data scientist or data analyst, more often than not, you may find yourself looking up the documentation of a particular function or plugin you use. Don't worry if there are a few functions you don't know by heart. However, there are just too many to know! An essential skill is to learn how to navigate documentation and understand how to apply the examples to your work.

Challenge
Can Dot spin a profit as an avocado farmer? Examine the data to find the average cost of avocados in Albany in 2017.
'''
import pandas as pd

df = pd.read_csv('avocado.csv', index_col = 0)
df.head()

df.groupby(['year','region']).mean().tail(110)

#Solution
#avo = df.groupby(['region','year']).mean()
#avo.head(20)
#avo.loc[('Albany', 2017)]

#My other solution:
#df.groupby(['year','region']).mean().loc[(2017, 'Albany')]
