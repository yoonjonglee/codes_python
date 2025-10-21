import sys
from collections import deque


# BFS Example using adjacency list

# 예시 그래프 (인접 리스트)

def bfs(graph, start):
    visited = set()        # 방문한 노드 기록
    dq = deque([start]) # 시작 노드를 큐에 넣기

    while dq:
        print(dq)
        node = dq.popleft()  # 큐에서 꺼내기
        if node not in visited:
            print(node)         # 방문 처리 (출력)
            visited.add(node)
            # 인접 노드를 큐에 추가
            dq.extend(graph[node])
            # .extend(...)` : 스택에 여러 개의 값을 **한 번에 추가** `append()`는 하나만 넣지만, `extend()`는 리스트나 튜플처럼 여러 값을 한 번에 넣을 수 있습니다.
            # `graph[node]` : 현재 노드(`node`)와 연결된 **인접 노드들의 리스트**를 가져옵니다. 예를 들어 `graph['A']`가 `['B', 'C']`라면, A와 연결된 노드는 B와 C입니다.

"""
BFS 탐색 순서:
1. 시작: A
2. A → B, C
3. B → D, E
4. C → F
5. D → (없음)
6. E → F(이미 방문)
7. F → (없음)

큐 변화 예시:
[ A ]
[ B, C ]
[ C, D, E ]
[ D, E, F ]
[ E, F ]
[ F ]
[ ]
그리고 이를 시각적으로 표현하면:

A
├── B
│   ├── D
│   └── E
└── C
    └── F
탐색 순서(번호로 표시):

A(1)
├── B(2)
│   ├── D(4)
│   └── E(5)
└── C(3)
    └── F(6)
"""

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
"""
A
├<──> B
│   ├<──> D
│   └<──> E
│       └<──> F
└<──> C
    └<──> F

Or

    A
   / \
  B   C
 / \   \
D   E -- F

"""

bfs(graph, 'A')