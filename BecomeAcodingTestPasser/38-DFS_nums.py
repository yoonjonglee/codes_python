import sys
import itertools
from collections import deque

# input
graph = [['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']] #[start, end]

# code here
def graph(graph, s):
    v = set()
    stack = []
    stack.append(s)
    while stack:
        n = stack.pop()
        if n not in v: v.add(n)
        else: stack.append(

s = graph
sol = graph(graph, s)

# output
print(sol)