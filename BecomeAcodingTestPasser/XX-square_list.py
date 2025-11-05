# Welcome to the Python coding playground.
# Return a list of squares from a given non-squared list of integers. The new list should be sorted in an ascending order. Try to find an O(n) solution.

# Sample program:
numbers = [-9, -3, 0, 1, 3, 4, 9, 12]
# [0, 1, 9, 9, 16, 81, 81, 144]

# Type your code here:
def sort_squares(ns):
    res = []
    for x in ns: res.append(x**2)
    # [81, 9, 0, 1, 9, 16, 81, 144]
    # 1. res.sort() # -> O(nlogn), worst case
    # 2. nested loop (bubble sort) -> O(n^2), worst case too
    """
    for x in range(1, len(res)):
        for y in range(len(res)-x):
            if res[y] > res[y+1]:
                t = res[y]; res[y] = res[y+1];res[y+1] = t
    """
    # 3. using two pointer method
    n = len(res); l = 0; r = n-1
    for i in range(n-1, -1, -1):
        ls = ns[l]**2; rs = ns[r]**2
        if ls > rs: res[i] = ls; l+=1
        else: res[i] = rs; r-=1
    print(res)

sort_squares(numbers)