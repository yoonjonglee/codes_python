import sys

"""
adjacency_matrix representation of a graph
ex = [[0, 400], # map
      [0, 0]]

adjacency list representation of a graph
ex1 = {0: [1], 1: []} # index: node number
ex2 = [[2, 3, 0] # dir, weight, [neighbors], index: node number
      , [1, 6, [3, 5, 0]]
      , [2, 1, [4, 13, 0]]
      , [4, 9, [1, 42, 0]]]
"""

# DFS Example using adjacency list

# way 1 - Using Stack
def dfs_stack(graph, start):
    visited = set()       # 방문한 노드 기록
    stack = [start]       # 시작 노드를 스택에 넣기

    while stack:
        node = stack.pop()  # 스택에서 꺼내기
        if node not in visited:
            print(node)     # 방문 처리 (출력)
            visited.add(node)
            # 인접 노드를 스택에 추가 (역순으로 넣으면 순서 제어 가능)
            stack.extend(reversed(graph[node]))
            # .extend(...)` : 스택에 여러 개의 값을 **한 번에 추가** `append()`는 하나만 넣지만, `extend()`는 리스트나 튜플처럼 여러 값을 한 번에 넣을 수 있습니다.
            # `reversed(graph[node])` : 그 리스트의 순서를 **뒤집습니다**. 스택은 LIFO(Last In, First Out) 구조이기 때문에, 뒤집어서 넣어야 원래 그래프의 순서대로 방문할 수 있습니다.
            # `graph[node]` : 현재 노드(`node`)와 연결된 **인접 노드들의 리스트**를 가져옵니다. 예를 들어 `graph['A']`가 `['B', 'C']`라면, A와 연결된 노드는 B와 C입니다.
"""
## 1. **스택을 이용한 DFS 흐름**
```
초기: stack = [A], visited = {}

1. pop A → 방문: visited = {A}
   push C, B → stack = [C, B]

2. pop B → 방문: visited = {A, B}
   push E, D → stack = [C, E, D]

3. pop D → 방문: visited = {A, B, D}
   (D의 인접 노드 없음) → stack = [C, E]

4. pop E → 방문: visited = {A, B, D, E}
   push F → stack = [C, F]

5. pop F → 방문: visited = {A, B, D, E, F}
   (F의 인접 노드 없음) → stack = [C]

6. pop C → 방문: visited = {A, B, D, E, F, C}
   push F → stack = [F]

7. pop F → 이미 방문 → stack = []

## 3. 시각적 비교
**스택 방식**  
```
[시작] → 스택에 넣고 → 꺼내서 방문 → 인접 노드 스택에 추가 → 반복
```
"""

# way 2 - Using Recursion
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)       # 방문 처리
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)
"""
## 2. **재귀를 이용한 DFS 흐름**
```
dfs(A):
  방문 A
  dfs(B):
    방문 B
    dfs(D):
      방문 D
    dfs(E):
      방문 E
      dfs(F):
        방문 F
  dfs(C):
    방문 C
    dfs(F):
      F는 이미 방문
```

---

## 3. 시각적 비교
**재귀 방식**  
```
[시작] → 방문 → 인접 노드로 함수 호출 → 깊게 들어감 → 더 이상 없으면 돌아옴
```
"""

# 예시 그래프 (인접 리스트)
"""
A
├── B
│   ├── D
│   └── E
│       └── F
└── C
    └── F
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

#dfs_stack(graph, 'A')
dfs_recursive(graph, 'A')