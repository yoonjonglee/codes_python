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
# way2 - O(N+K), better way for lower complexity (without nested loop)
def solve():
    dic = Counter(li) # O(N), dic is a dictionary of the list
    cv = list(dic.items()) # O(K), cv is a list of the dictionary
    for x in range(len(cv)):
        k=t-cv[x][0] # k is the target value - the current value
        if k < len(cv) and 1 == dic[k]: # check if the target value is in the dictionary and the value is 1
            return True # if the target value is in the dictionary and the value is 1, return True
    return False # if the target value is not in the dictionary or the value is not 1, return False

print(solve())