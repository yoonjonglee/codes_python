from collections import Counter
# 8. find 2 numbers to make the target value
# make_2nums_value.py

li = [1,2,3,4,8]; t=6 # True
#li = [2,3,5,9]; t=10 # False

# way1 - O(N**2), bad way
"""
def solve():
    n = len(li)
    for i in range(n):
        for j in range(i+1, n):
            if t == li[i]+li[j]: return True
    return False
"""
# way2 - O(N+K), better way
def solve():
    dic = Counter(li)
    cv = list(dic.items())
    for x in range(len(cv)):
        k=t-cv[x][0]
        if k < len(cv) and 1 == dic[k]:
            return True
    return False

print(solve())