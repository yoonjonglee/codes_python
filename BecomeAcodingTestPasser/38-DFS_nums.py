import sys
from collections import defaultdict
#import itertools
#from collections import deque

# input
#graph = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']] #[start, end]
graph = [['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']] 

# code here

al = defaultdict(list)
#v = set()
v = []
stack = []

def DFS(graph, start):
    for s, e in graph:
        al[s].append(e)
    stack=[start]
    while stack:
        #print(stack)
        n = stack.pop()
        if n not in v: 
            #v.add(n)
            v.append(n)
            stack.extend(reversed(al[n]))
    
    return list(v)

sol = DFS(graph, 'A')

# output
print(sol)