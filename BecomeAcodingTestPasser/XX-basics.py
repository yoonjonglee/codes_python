import sys
import itertools
from collections import deque

## 1. manhattan distance
#input
p1 = [5, 8]
p2 = [3, 6]
#code here
#md = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
"""
격자(grid) 상태에서 맨해튼 거리는 항상 최단 거리가 맞습니다. 
이는 맨해튼 거리의 정의 자체가 격자형 도로망을 따라 이동할 때의 최단 거리를 의미하기 때문
"""
#output
#print(md)

## 2. permutations
#input
d = ['A', 'B', 'C']

#code here
#p = itertools.permutations(d) # 모든 순열 생성
#p = itertools.permutations(d, 2) # 2개씩 뽑는 모든 순열 생성
#sol = [list(x) for x in p]

#output
#print(sol)

## 3.1. DFS - stack, adjacency list

#input
graph = {1: [4, 5], 2: [3], 3: [], 4: [2, 3], 5: [4]}
s = 1 # start node
#code here
def dfs_stack(graph, s):
    v = set()      # 방문한 노드 기록
    stack = [s]   # 시작 노드를 스택에 넣기
    while stack:
        print(stack)
        node = stack.pop()  # 스택에서 꺼내기
        if node not in v:
            v.add(node); print(node)       # 방문 처리 (출력)
            stack.extend(reversed(graph[node])) # 인접 노드를 스택에 추가

#dfs_stack(graph, s)

## 3.2. DFS - recursion, adjacency list

#code here
def dfs_recursive(graph, s, v):
    if s not in v:
        v.add(s); print(s) # 방문 처리 (출력)
        for n in graph[s]:
            dfs_recursive(graph, n, v)

#dfs_recursive(graph, s, v=set())

## 4. BFS - queue, adjacency list

#code here
def bfs(graph, s):
    v = set() #     방문한 노드 기록
    dq = deque([s]) # 시작 노드를 큐에 넣기
    while dq:
        print(dq)
        node = dq.popleft() # 큐에서 꺼내기
        if node not in v:
            v.add(node); print(node) # 방문 처리 (출력)
            dq.extend(graph[node]) # 인접 노드를 큐에 추가

# bfs(graph, s)

## 5.1. sorting - move zeros to end

#input
arr = [5, 2, 0, 9, 0, 1, 0, 5, 0, 6]

#code here. but don't make a new list
# nested loop way
def move_zero_to_end(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] != 0 and n[j] == 0 and i > j: # find non-zero at i and zero at j
                n[j]=n[i] ; n[i] = 0 # swap
    print(n)
"""
# double loop way
def move_zero_to_end(n):
    non_zero_index = 0  # This will track the position for non-zero elements

    for i in range(len(n)):
        if n[i] != 0:  # Check if the current element is not zero
            n[non_zero_index] = n[i]  # Move it to the front
            non_zero_index += 1  # Increment the index for next non-zero

    # Fill remaining positions with zeros
    for i in range(non_zero_index, len(n)):
        n[i] = 0
    print(n)
"""
#output
# move_zero_to_end(arr)

# 5.2. sorting - custom sort with lambda
#l = [[10, 19], [7, 10], [6, 10]]
d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}
#sol = sorted(l, key = lambda item: item[1])
#sol = sorted(l, key = lambda item: item[1], reverse = True)
#sol = dict(sorted(d.items())) # sort dict by key
#sol = dict(sorted(d.items(), reverse = True)) # sort dict by key
sol = dict(sorted(d.items(), key=lambda item: item[1])) # sort dict by whole value
#sol = dict(sorted(d.items(), key=lambda item: item[1][1])) # sort dict by 2nd value
"""
1. **`d.items()`**  
   - 딕셔너리의 `(key, value)` 쌍을 튜플 형태로 반환합니다.  
   - 예:  
     ```python
     d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}
     list(d.items())
     # [('A', [10, 19]), ('B', [7, 10]), ('C', [6, 10])]
     ```
2. **`key=lambda item: item[1][1]`**  
   - `item`은 `(key, value)` 튜플입니다.  
   - `item[1]` → value 부분 (`[10, 19]` 같은 리스트)  
   - `item[1][1]` → value 리스트의 두 번째 요소 (예: `19`, `10`, `10`)  
   - 즉, 정렬 기준을 “value의 두 번째 값”으로 지정하는 것입니다.
"""
print(sol)