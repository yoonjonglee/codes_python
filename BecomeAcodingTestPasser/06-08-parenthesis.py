import sys

#input argument
inputs = sys.stdin.readline
'''
((((())))) ...
)가 들어오면, 스택안에 있는 (를 팝
(가 들어오면, 스택에 (를 푸시


'''
sol = -1

#code here
def solve(inputs):
    stack = []
    for c in inputs:
        if c == '(':
            stack.append(c)
        


sol = solve(inputs)

# output
print(sol)