import sys

#input argument
inputs = sys.stdin.readline
'''
((((())))) ...
()()(())
)가 들어오면, 스택안에 있는 (를 팝
(가 들어오면, 스택에 (를 푸시


'''
inputs = inputs().strip()
sol = -1

#code here
def solve(inputs):
    stack = []
    for c in inputs:
        if c == '(': stack.append(c)
        elif c == ')':
            if stack: stack.pop()
            else: return False
    if len(stack) == 0: return True
    else: return False

sol = solve(inputs)

# output
print(sol)