'''
Tutorial
While working with data, we may want to figure out the frequency distribution of a numerical dataset. The frequency distribution refers to how often each value occurs within a dataset. This can be important to know so that we can understand whether the data we are analyzing is normally distributed or skewed.
The best way to visualize the distribution of our dataset is with a histogram. Histograms are a graphical representation of data using bars of different heights. Similar to bar charts, histograms group numbers into buckets. The size of each bar shows how many fall into each range.

Building a histogram with MatPlotLib
Here is how a histogram can be built using Matplotlib:
plt.figure()
plt.hist(df['numerical_data'], bins = 40) #Play around with the bin sizes when plotting your histogram
plt.show()

Normal Distribution
A histogram with the following characteristics would have a normal distribution:
the mean & the median are the same.
1 standard deviation from the mean captures 68.2% of the data.
2 standard deviation from the mean capuures 95.4% of the data.

Skewed Distribution:
Within this image, we can see the two types of skewed distribution:

Challenge
1. What type of distribution does the column avg_time have?
2. Do games that have a great avg_rating have longer play times?
Note: For question 2, filter out games that have are above the avg_rating of 9.0.
'''
#Q1
plt.figure()
plt.hist(df['avg_time'], bins=30) #Play around with the bin sizes when plotting your histogram
plt.show()

#Q2
filtered_df = df[df['avg_rating']>=9.0]
if filtered_df.avg_time.mean() - df.avg_time.mean() > 0:
    print('yes')
else:
    print('no')
