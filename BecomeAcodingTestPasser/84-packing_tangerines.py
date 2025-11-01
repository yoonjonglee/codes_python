# finding the numbers of smalleast gaps in packing tangerines
# 1<=numbers of tangerines<=100000
# 1<=numbers per one pack <=10000000

#input
k = 6; ts = [1,3,2,5,4,5,2,3] # 3
#k = 4; ts = [1,3,2,5,4,5,2,3] # 2
#k = 2; ts = [1,1,1,1,2,2,2,3] # 1

#code here
#1:1, 2:2, 3:2, 4:1, 5: 2
#1:4, 2:3, 3:1
dic = {}
sts = set(ts)
for x in sts:
    dic[x] = ts.count(x)
sdic = dict(sorted(dic.items(), key=lambda x: x[1])) # {1: 1, 4: 1, 2: 2, 3: 2, 5: 2}, sorted by value
# print(sdic)
# find the smallest gap between the numbers for value added up to k

#output
#print(cnt)