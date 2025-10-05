import sys




def input():
    input = sys.stdin.readline
    return input

# input
path = input()
'''
exmaple input
ULURRDLLU, LULLLLLLU. ...

expected output
7, 7, ...
'''
sol = -1
#code here
def solve(path):
     dir = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
     current = [0, 0]
     for i in path:
          if i == 'U':

sol = solve(path)

#output
print(sol)