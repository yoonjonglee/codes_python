import sys

# input
li = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

# code here
def solve(li, target):
    l, r = 0, len(li) -1
    while l <= r:
        mid = (l + r) //2
        if li[mid] == target: return mid
        elif li[mid] < target: l = mid + 1
        else: r = mid -1

sol = solve(li, target)

# output
print(sol)