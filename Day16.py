'''
Tutorial
In the past challenges, we've encountered problems where we've had to determine the mean or maximum values of a numeric column or a range of numeric values.
Using pandas, a function that's been helpful for us was df. describe(). This function does a great job summarizing the descriptive statistics of numerical columns in a pandas DataFrame.

But what if we wanted to visualize the descriptive statistics of a range of numeric values. What would be the most effective way?

The best plot for summarizing descriptive statistics would be a boxplot. A boxplot can visually provide us with the following information:

Median
Interquartile Range (IQR)
Q1
Q3
Q1 - 1.5*IQR
Q3 + 1.5*IQR
Outliers
Boxplot Example

plt.figure()
plt.boxplot(df.['numerical_data'])
plt.show()

Challenge
Create a boxplot to answer the following questions:

How many books have over 4000 pages?

Note: Do not use a fitler, use a boxplot.

What are the average ratings for books that have over 4000 pages?

Note: You can use a filter for question 2.
'''

import pandas as pd
import matplotlib.pyplot as plt
# Given
df = pd.read_csv("books.csv")

# Plot
plt.figure()
plt.boxplot(df['num_pages'])
plt.show()

# Actual solutions
filtered_df = df[(df['num_pages']>4000)]
num_of_book_more_than_4000_pages = len(filtered_df)
print(num_of_book_more_than_4000_pages)
avg_rating = filtered_df['average_rating']
print(avg_rating)
