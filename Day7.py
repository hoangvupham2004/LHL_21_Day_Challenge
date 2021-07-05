#example dictionary
user_boxes = {'weight': [4,2,18,21,14,13],
              'box_name': ['box1','box2', 'box3', 'box4', 'box5', 'box6']
             }

#weight
weight = [4,2,18,21,14,13]
sorted_weight = sorted(weight)
print(sorted_weight)

#box name
box_name = ['box1','box2', 'box3', 'box4', 'box5', 'box6']
sorted_box = []

for i in range(len(sorted_weight)):
    value = sorted_weight[i]
    #print(weight.index(value))
    #print(box_name[weight.index(value)])
    sorted_box.append(box_name[weight.index(value)])
print(sorted_box)


#def open_box_order(lst):
#    for i in range(len(lst)):
#        for j in range(len(lst) - 1):
#            if lst[j] > lst[j+1]:
#                lst.insert(j+2, lst[j])
#    return print(lst)

#print(open_box_order(user_boxes['weight']))
