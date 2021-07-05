'''
Challenge
Help Dot by answering the following questions using a bar plot:

What are the top 5 rated books in the dataset?

What are the top 5 books with the highest average rating?

Note: Filter out books that have low ratings_count, for question 2 filter out books with a ratings_count less than the mean.

Stretch

As an optional bonus question, try answering this as well:

What are the top 5 authours with the most books in the dataset?
'''

import pandas as pd
import matplotlib.pyplot as plt

# Given
df = pd.read_csv("books.csv")
df.head(2)

# Q1
df.sort_values(by=['ratings_count'], ascending=False)
list(df['title'].head(5))

# Q2
df = df[df['ratings_count']<df['ratings_count'].mean()]
df.sort_values(by=['average_rating'], ascending=False)
list(df['title'].head(5))

# Note: the provided answers and actual answers are different...
