'''
Tutorial
In today's challenge, we're going to look at some fundamental stylistic methods we can use to improve our plots. The simple plots we've been creating have been quite bare. There are no titles, the fonts are small, the size of the plots may be small, the colour may not match your liking, there isn't a legend...the list can go on.

Here are some of the basic ways we can add style to our plots using Matplotlib:

Matplotlib stylistic functions:

plt.figure(figsize = (14,7)) #declaring the figsize will give the user control to shape the figure to size/shape the user wants.
plt.bar(df['categorical_data'], height = df['categorical_data'], color = 'red') #We can specify the color of our columns, default is blue
plt.xlabel('This is the x axis!', fontsize = 14) #Specify a title for the x axis
plt.xticks(rotation = 'vertical') #Specifying a roation to the x ticks, to make it easier to view large strings
plt.ylabel('This it the y axis!', fontsize = 14) #Specify a title for the y axis
plt.show()

Challenge¶
1. What are the top 5 boardgame categories in this dataset that are not targeted for young children?
Note: For the question above, use a filter to acquire boardgames with an inteded age of 13+, there is an age column in our dataset.
2. Which categories of boardgames that are not targeted for young children are the same compared to the top 5 boardgames categories in the overall dataset?
'''
#Given
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('boardgames.csv')
df.head(2)

#Q1
filtered_df = df[df['age']>=13]
filtered_top_5 = list(filtered_df.category.value_counts().head().index)

#Q2
original_top_5 = df.category.value_counts().head().index
category_in_original_and_filtered_df = []
for category in filtered_top_5:
    if category in original_top_5:
        category_in_original_and_filtered_df.append(category)
