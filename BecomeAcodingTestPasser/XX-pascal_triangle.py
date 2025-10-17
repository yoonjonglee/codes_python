import sys

inputs = sys.stdin.readline

#n = int(inputs())
n = 8
# code here
t = [[1]] # first row

for x in range(1, n): # build row x
    pr = t[x-1] # previous row
    nr = [1] # new row
    for y in range(len(pr)-1): # build middle values
        nr.append(pr[y]+pr[y+1]) # sum of two above
    nr.append(1) # last value
    t.append(nr) # add new row

# output
mx = len(" ".join(map(str, t[-1]))) # row max number length
for r in t: # for each row
    s = " ".join(map(str, r)) # row as string
    print(s.center(mx)) # center aligned
"""
  1  
 1 1 
1 2 1
"""

