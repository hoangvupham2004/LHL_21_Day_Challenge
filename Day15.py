Day 15
'''
Dot already has a few seeds they can use for their garden. They need to figure out which of the seeds will produce the biggest potential harvest.
Can you help Dot decide which seeds are best, by using data visualization?

Create a bar graph with Matplotlib that shows each vegetable and the size of the potential harvest that Dot can expect from them.

Which of Dot's seeds will produce the largest harvest?

import matplotlib.pyplot as plt

plt.figure() #The Frame: We start our plot with a figure
plt.bar(x = data, height = data) #The Body: Declaring the specific bar plot statment
plt.title("Example Bar Plot") #Stylistic Features: Adding the title
plt.show() #To show our plot, we need to end our plot with a plt.show()

Below is an example code to produce a simple bar chart. Try it out yourself!

data = {'item_1':40, 'item_2':50, 'item_3':25}
items = list(data.keys())
quantity = list(data.values())


plt.figure()
plt.bar(x = items, height = quantity)
plt.show()
'''

import pandas as pd
import matplotlib.pyplot as plt
# Given
seeds = {
    'Vegetable' : ['Carrots', 'Tomatoes', 'Potatoes', 'Eggplant', 'Cucumbers'],
    'Seeds_Count' : [300,10,90,100,15],
    'Each_Seed_Produces': [1,140,10,5, 90]
}

df = pd.DataFrame(seeds)
print(df)

df['Harvest']=df['Seeds_Count']*df['Each_Seed_Produces']

# plot
plt.figure()
plt.bar(x = df['Vegetable'], height = df['Harvest'])
plt.title('The seeds that will produce the largest harvest')
plt.show()
