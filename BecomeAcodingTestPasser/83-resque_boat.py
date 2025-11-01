# find how many boats are needed at least for resqueing.
# 1<=number of people<=50000
# 40<=weights of people<=240
# 40<=weight limit of the boat<=240

#input
pe = [70,50,80,50] # weights of people
#pe = [70,80,50] # weights of people
lm = 100 # weight limit of the boat 

#code here
spe = sorted(pe) # 50, 50, 70, 80
cnt = 0; s = 0; b = len(spe)-1 # s: start index(small), b: end index(big)
while s <= b:
    if spe[s] + spe[b] <= lm: # if the weight of the two people is less than or equal to the weight limit of the boat, then they can share the boat
        s+=1 # take the two people - small one and big one
    b-=1 # take the big one only
    cnt+=1 # count the number of boats
#output
print(cnt)