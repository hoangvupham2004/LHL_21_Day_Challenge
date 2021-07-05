'''
After purchasing all the supplies they needed to make repairs, Dot's house is starting to look incredible. The floors
are patched, and the rooms are painted to perfection. Now all they need is to give the house a good thorough cleaning.
The bad news is that the box with their cleaning supplies seems to have been misplaced in the move.

The store in the nearby town does sell cleaning supplies, but their prices can sometimes be a lot higher than Dot's
used to. They've already spent so much money on repairs - can you help them figure out which supplies to abstain from
buying at the town's store?

Dot's okay with paying a bit of a surplus for convenience, but they don't want to go broke buying dustpans and
glass cleaner. Help them figure out which items cost over 10% more at the nearby store, so they can avoid buying
these items.
Using Python, develop a list of items that are too expensive for Dot to purchase at the nearby store.
'''
#"Dot's okay with paying a bit of a surplus for convenience, but they don't want to go broke buying
#dustpans and glass cleaner. Help them figure out which items cost over 10% more at the nearby store,
#so they can avoid buying these items."

# Cleaning Supplies List (19 items)
cleaningsupplies_list = ['Broom', 'Mop', 'Dustpan', 'Garbage Bags', 'Glass Cleaner', 'Vinegar',
                        'Soap', 'Bleach', 'Duster', 'Floor Cleaner', 'Sponges', 'Dish Soap',
                        'Drain Cleaner', 'Paper Towels', 'Cleaning Rags', 'Toilet Cleaner',
                        'Rubber Gloves', 'Alcohol Wipes', 'Squeegee']

# City Price
city_price = [6.49, 4.99, 3.39, 4.29, 3.99, 1.99,
              1.50, 3.99, 4.99, 5.99, 2.99, 2.99,
              5.99, 2.99, 3.49, 6.99, 2.99, 1.98, 11.99]

# Country Price
country_price = [5.49, 4.69, 4.42, 5.99, 5.99, 2.50,
                1.25, 2.49, 4.50, 6.75, 2.49, 1.99,
                6.25, 3.99, 3.59, 4.99, 1.69, 1.87, 10.99]

expensive = []
for i in range(len(cleaningsupplies_list)):
    #Dot lives in the country
    value = (country_price[i]-city_price[i])/city_price[i]
    if value > 0.1:
        expensive.append(cleaningsupplies_list[i])
print(expensive)
