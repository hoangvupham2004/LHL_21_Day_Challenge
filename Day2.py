# Grocery List (19 items)
grocery_list = ['Bananas', 'Clementines', 'Baguette', 'Oat Milk', 'Olive Oil', 'Coffee Beans',
                'Chocolate Bar', 'Brocolli', 'Eggplant', 'Chickpeas', 'Lentils', 'Tomatoes',
                'Pasta', 'Rice', 'Yogurt', 'Blueberries', 'Onions', 'Garlic', 'Truffles']

# City Price
city_price = [6.49, 4.99, 4.39, 4.29, 11.99, 17.99,
              3.49, 3.99, 1.10, 1.99, 2.99, 4.68,
              1.59, 8.99, 3.49, 6.99, 2.99, 1.98, 14.99]

# Country Price
country_price = [4.49, 4.12, 3.42, 6.99, 7.99, 14.99,
                2.99, 2.49, 0.99, 1.49, 2.49, 1.99,
                1.59, 6.99, 3.89, 4.99, 1.69, 1.87, 11.49]

city=0
country=0

#No need for such complicated methods
# for each in range(len(city_price)):
#    difference = (city_price[each]-country_price[each])/country_price[each]
#    print(grocery_list[each], " city: ", city_price[each], " country: ", country_price[each], " percent: ", difference)
#    percent.append(difference)
#    total = total + difference
# print(total/len(city_price))

for each in range(len(city_price)):
    city = city + city_price[each]
    country = country + country_price[each]

percent = (city - country) / country
print(round(percent,4))

#or according to another source
city2=(sum(city_price))
country2=(sum(country_price))
difference=(city2-country2)/country2
print(difference)

