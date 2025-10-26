import sys

# input
wl = 15
items = [[10, 19], [7, 10], [6, 10]]

# code here
# calculate value per kg and add to each item
for x in range(len(items)):
    vokg = items[x][1] / items[x][0]
    items[x].append(vokg)

# sort items by value per kg in descending order    
sl_vokg = sorted(items, key = lambda item: item[2], reverse = True)

fv = 0 # final value
# loop through sorted items and add to knapsack
for x in range(len(sl_vokg)):
    cl = wl - sl_vokg[x][0] # current load after adding item
    # check if current load is positive
    if cl > 0:
        fv = fv + sl_vokg[x][0] * sl_vokg[x][2] # add full item value
        wl = cl # update weight left
    # if current load is negative, add fractional item
    else:
        fv = fv + wl * sl_vokg[x][2] # add fractional item value
        wl = 0 # knapsack is full

#output
print(fv)