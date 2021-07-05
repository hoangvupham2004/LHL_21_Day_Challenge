'''
Use a loop to determine the price Dot would pay for purchasing supplies at the retail price. Based on that calculation,
which itmes should Dot buy at retail vs. wholesale?
Note: Assume the wholesale price covers all the supply Dot needs for each item, whereas the retail price is per single unit.
'''
#raw data
item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']
amount_list = [600,150,15,165]
wholesale_price_list = [7000, 1000, 1000, 800]
retail_price = [12.99, 8.99, 9.99, 3.99]

#create a new list for the total cost of items if we buy at retail price
total_retail_price = []
#use the len function to get the size of the item_list, then use the range function to get (0,4)
for i in range(len(item_list)):
    total_retail_price.append(amount_list[i]*retail_price[i])
    if wholesale_price_list[i] > total_retail_price[i]:
        print(item_list[i] + " Wholesale? No")
    else:
        print(item_list[i] + " Wholesale? Yes")




#EXTRAAF
#build a new dictionary
list_and_pricing = {item:{"amount":{},"whole sale price":{}, "unit retail price":{}, "total retail price":{},
                          "Wholesale?":{}} for item in item_list}
#to check the initial dictionary
#print(list_and_pricing)

i=0
for item in list_and_pricing:
    #enter the given data into created dictionary
    list_and_pricing[item]["amount"] = amount_list[i]
    list_and_pricing[item]["whole sale price"] = wholesale_price_list[i]
    list_and_pricing[item]["unit retail price"] = retail_price[i]
    #calculate total retail price
    list_and_pricing[item]["total retail price"] = amount_list[i]*retail_price[i]
    #comparison whether wholesale or not
    if list_and_pricing[item]["whole sale price"] > list_and_pricing[item]["total retail price"]:
        list_and_pricing[item]["Wholesale?"] = "No"
    else:
        list_and_pricing[item]["Wholesale?"] = "Yes"
    #counter
    print(item_list[i], list_and_pricing[item])
    i = i + 1

#shortened table
i=0
for item in list_and_pricing:
    print(item_list[i], " Wholesale? ", list_and_pricing[item]["Wholesale?"])
    i = i + 1
#to check the final dictionary
#print(list_and_pricing)
