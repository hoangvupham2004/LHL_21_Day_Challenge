old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
    "Bedroom" : ["Clean", 'Mahogany', 'Good Condition', 'Green'],
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition','White'],
    "Shed"    : ['Dirty', "Cherry", "Damaged", "Un-painted"]
}

new_shopping_list = ['20 x Oak plank', '20 x Oak Plank', '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']

paint_list = new_shopping_list[3]
print(paint_list)

paint_list = new_shopping_list[:3]
print(paint_list)

paint_list = new_shopping_list[3:]
print(paint_list)

paint_list = new_shopping_list[4:9]
print(paint_list)

paint_list = new_shopping_list[4:]
print(paint_list)
