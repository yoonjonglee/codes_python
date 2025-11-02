from collections import Counter
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
cnt = 0; sum = 0
#dic = {} - not needed
#sts = set(ts) - not needed
#for x in sts: - not needed
#    dic[x] = ts.count(x) - not needed
dic = Counter(ts)
# 파이썬의 collections 모듈에 있는 Counter는 리스트나 문자열 같은 반복 가능한(iterable) 객체에서 
# 각 요소가 몇 번 등장했는지를 세어 딕셔너리 형태로 반환. - # {1: 1, 2: 2, 3: 2, 4: 1, 5: 2}
sdic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
# {2: 2, 3: 2, 5: 2, 1: 1, 4: 1}, sorted by value reverse
#sdic = sorted(dic.values(), reverse=True) # -> [2, 2, 2, 1, 1]. use this when you solve by list. below is by dictionary.
# find the smallest gap between the numbers for value added up to k
for x in sdic:
    sum += sdic[x] # sum of values
    cnt += 1 # count of keys
    if sum >= k: 
        break # if sum is greater than or equal to k, break
#output
print(cnt)