from collections import deque
from collections import defaultdict

# input
#graph = [(1, 2),(1, 3),(2, 4),(2, 5),(3, 6),(3, 7),(4, 8), (5, 8),(6, 9), (7, 9)] #[start, end]
graph = [(0, 1),(1, 2),(2, 3),(3, 4),(4, 5),(5, 0)]
# output
al = defaultdict(list)
v = []
dq = deque()

def BFS(graph, start):
    for s, e in graph:
        al[s].append(e)
    print(al)
    dq.append(start)
    while dq:
        #print(dq, v)
        n = dq.popleft()
        if n not in v:
            v.append(n)
            dq.extend(al[n])
    
    return v

sol = BFS(graph, 1)

# output
print(sol)