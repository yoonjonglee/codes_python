import sys
from collections import deque

inputs = sys.stdin.readline
n, k = map (int, inputs().split())
"""
1 2 3 4 5, n=5, k=2
3 4 5 1 # 2(k = 2) was removed
5 1 3   # 4(k = 2) was removed
3 5     # 1(k = 2) was removed
3       # 5(k = 2) was removed
"""

# code here
def solve(n, k):
    dq = deque(range(1, n+1)) # 1~n
    cnt = 0 # count for k
    while len(dq) > 1:  # until only one element remains
        cnt += 1 # increment count
        if cnt == k: dq.popleft(); cnt = 0 # remove element
        else: dq.append(dq.popleft()) # rotate the deque
        #print(dq)
    return dq

sol = solve(n, k)
# output
print(sol)