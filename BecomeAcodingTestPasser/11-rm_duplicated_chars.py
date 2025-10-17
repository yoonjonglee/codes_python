import sys

# input
s = input()
sol = -1

# code here
stack = []
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
    else:
        stack.append(c)

if len(stack) == 0: sol = 1
else: sol = 0


# output
print(sol)