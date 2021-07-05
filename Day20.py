Day 20
'''
Building a scatterplot with Matplotlib

Here is how a scatterplot can be built using Matplotlib:
plt.figure()
plt.scatter(x = df['numerical_data'], y = df['numerical_data_2'])
plt.show()

Determining Correlation in Pandas?
In addition to creating a scatter plot to view relationships between two numerical ranges. Pandas also has a built-in function that outputs the correlation value for us:
pd.DataFrame.corr()
The correlation coefficient is given to us from a range of -1 to 1. Values closer to -1 indicate a negative correlation, whereas values closer to 1 indicate a positive correlation.

Challenge¶
Play around with the scatterplot and test out different correlations between the numerical categories in the dataset. Then, help Dot by answering these questions:
1. What kind of correlation is there between the weight and avg_rating?
2. What is the correlation coefficient between the two columns?
'''
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('boardgames.csv')
df.head(3)

#Q1
df['weight'].corr(df['avg_rating'])

