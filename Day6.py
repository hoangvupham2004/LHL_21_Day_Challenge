#function to generate pseudo-random numbers
import random
#.seed is a book keeping function, where 34 is the seed number. Note --> same seed same "random"
#number every time
random.seed(34)

#.randint generate a randome number within the range of (start, end)
hole_sizes = [random.randint(1, i) for i in range(1, 101)]
print("This is how the numbers actually look like")
print(hole_sizes, "\n")
#the "seemingly random" numbers now could be truely random, but how can it be the same every time... --> seed?
random.shuffle(hole_sizes)

# hole sizes in mm
print("After shuffle")
print(hole_sizes)

# x < 20mm - $1.30
# 20mm < x < 70mm - $1.60
# x > 70mm - $2.10

#pandas is a python plugin, used for data cleaning and manipulation
import pandas
#converting the hole sizes list to a pandas series variable for various functions below
new_hole_sizes = pandas.Series(hole_sizes)

#2
cost = []
for i in range(len(hole_sizes)):
    if hole_sizes[i] < 20:
        cost.append(1.30)
    elif hole_sizes[i] >= 20 and hole_sizes[i] < 70:
        cost.append(1.60)
    else:
        cost.append(2.10)
new_cost = pandas.Series(cost)

print("\nAverage sized hole = ", new_hole_sizes.mean(), "mm")
print("Average cost to fix a hole = $", round(new_cost.mean(), 3))
print("Average cost to fix a hole = $", round(new_cost.sum(), 2))
print("Max sized hole = ", new_hole_sizes.max(), "mm")
print("Min sized hole = ", new_hole_sizes.min(), "mm")
