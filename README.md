# codes_python
## 주요 측정 항목
- List, Stack - [ ].append()
- Queue(Deque) - deque().append()
- Binary Search (이진 검색)
- Greedy
- BFS, DFS
- Flood Fill

## [ 2개의 주사위가 나올수 있는 모든 경우의 수 인쇄]

### [1] for 2개로 할 경우

```
for i in range(1,7):
    for j in range(1, 7):
    print(i, j)
```
-----------

### [2] 중복순열구조
```
sol = [0]*4
chk = [0]*7
def DFS(n):
    if n>2:
        print(sol)
        return

for i in range(1, 7):
    sol[n]=i
    DFS(n+1)

DFS(1)
```
-----------
### [3] 순열구조(중복배제)

```
sol = [0]*4
chk = [0]*7
def DFS(n):
    if n>2:
        print(sol)
        return


for i in range(1, 7):
    if chk[i]==1: continue
    chk[i]=1
    sol[n]=i
    DFS(n+1)
    chk[i]=0

DFS(1)
```
-----------
### [4] 조합구조

```
sol = [0]*4
chk = [0]*7
def DFS(n, start):
    if n>2:
        print(sol)
        return

    for i in range(start, 7):
        sol[n]=i
        DFS(n+1, i+1) # i 면 중복 조합

DFS(1, 1)
```

-------------------------------------------

## [선택유무에 따른 이중재귀로 조합구조 ]

### [1] 3개의 정수를 고르는 모든 경우의 수

```
arr = [3, 4, 7]
box = [0]*3

def DFS(n):
    if n>=3:
        print(box)
        return
    box[n]=arr[n]
    DFS(n+1)
    box[n]=0
    DFS(n+1)

DFS(0)    
```
-----------

### [2] 정수중 일부 합산하여 7이 되는 모든 경우의 수

```
arr = [3, 4, 7, 10]
box = [0]*4

def DFS(n, tot):
    if tot>7: return #가지치기
    if n>=4:
        if tot==7: print(box)
        return
    box[n]=arr[n]
    DFS(n+1, tot+arr[n])
    box[n]=0
    DFS(n+1, tot)

DFS(0, 0) 

```
--------------------------------

## [ 백준 OJ (www.acmicpc.net)에서 풀어볼 만한 문제 ] 

### 1. DFS

- N과 M 시리즈 (https://www.acmicpc.net/workbook/view/2052) - DFS에 자신이 없으시다면 꼭 풀어보세요. 다양한 경우의 수 모델에 대해 DFS코드를 작성하는 방법을 공부 할 수 있습니다.
- 6603 로또 (실버2)
- 10819 차이를 최대로(실버2)
- 16922 로마 숫자 만들기 (실버3)
- 10971 외판원 순회(실버2)
- 2529 부등호 (실버1)
- 14888 스타트와 링크 (실버1)
- 2529 부등호 (실버1)
- 2580 스도쿠 (골드4)
- 1759 암호 만들기(골드5)
- 6987 월드컵 (골드4)
- 9207 페그 솔리테어 (골드4)
- 1248 Guess(골드3)

### DFS(Depth-First Search)을 파이썬에서 **스택**과 **재귀**로 각각 구현하는 방법

---

#### 1. DFS 개념 간단 정리
DFS는 **깊이 우선 탐색**으로, 한 노드에서 시작해 가능한 한 깊게 내려간 뒤, 더 이상 갈 곳이 없으면 뒤로 돌아와 다른 경로를 탐색하는 방식입니다.  
즉, "한 길로 끝까지 가보고, 막히면 돌아와서 다른 길로" 라고 생각하면 됩니다.

---

#### 2. 스택을 이용한 DFS (반복문 방식)
스택은 "마지막에 넣은 것을 먼저 꺼내는" 자료구조입니다. DFS는 이 특성을 잘 활용합니다.

```python
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

# 예시 그래프 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs_stack(graph, 'A')
```

**동작 흐름**  
1. 시작 노드를 스택에 넣음  
2. 스택에서 꺼내서 방문  
3. 방문하지 않은 인접 노드를 스택에 넣음  
4. 스택이 빌 때까지 반복  

---

#### 3. 재귀 함수를 이용한 DFS
재귀는 "함수가 자기 자신을 호출"하는 방식입니다. DFS는 깊게 들어갔다가 돌아오는 구조라 재귀와 잘 맞습니다.

```python
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    if node not in visited:
        print(node)       # 방문 처리
        visited.add(node)
        for neighbor in graph[node]:
            dfs_recursive(graph, neighbor, visited)

# 같은 그래프 사용
dfs_recursive(graph, 'A')
```

**동작 흐름**  
1. 현재 노드를 방문  
2. 인접 노드로 재귀 호출  
3. 더 이상 방문할 노드가 없으면 함수가 종료되며 이전 단계로 돌아감  

---

#### 4. 차이점 정리
- **스택 방식**: 반복문으로 구현, 명시적으로 스택 자료구조를 사용  
- **재귀 방식**: 함수 호출 스택을 이용, 코드가 간결하지만 깊이가 너무 깊으면 `RecursionError` 발생 가능  
- **공통점**: 방문 여부를 기록해야 무한 루프 방지  

----------------------------------
### 2. BFS
- 1697 숨바꼭질 (실버1)
- 1389 케빈 베이컨의 6단계 법칙 (실버1)
- 21937 작업 (실버1)
- 16927 뱀과 사다리 게임(골드5)
- 2589 보물섬(골드5)
- 9019 DSLR (골드4)
- 13013 숨바꼭질4 (골드4)
- 12886 돌 그룹 (골드4)
- 2206 벽 부수고 이동하기 (골드3)
- 5972 택배 배송 (골드5)
- 1283 파티 (골드3)
- 10282 해킹 (골드4)

### BFS(Breadth-First Search)를 큐를 이용해서 구현하는 방법

BFS는 **너비 우선 탐색**으로, 시작 노드에서 가까운 노드부터 차례대로 탐색하는 알고리즘입니다.  
이때 **큐(Queue)** 자료구조를 사용하면, 방문할 노드를 순서대로 관리할 수 있습니다.  

---

#### BFS 동작 흐름
1. **시작 노드를 큐에 넣는다.**
2. 큐에서 노드를 꺼내서 방문 처리한다.
3. 해당 노드의 **아직 방문하지 않은 인접 노드**를 큐에 넣는다.
4. 큐가 빌 때까지 2~3 과정을 반복한다.

---

#### 파이썬 예제
```python
from collections import deque

def bfs(graph, start):
    visited = set()          # 방문한 노드를 기록
    queue = deque([start])   # 시작 노드를 큐에 넣기

    while queue:
        node = queue.popleft()  # 큐에서 꺼내기
        if node not in visited:
            print(node)         # 방문 처리 (출력 예시)
            visited.add(node)

            # 인접 노드 중 방문하지 않은 노드를 큐에 추가
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# 예시 그래프 (인접 리스트)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

bfs(graph, 'A')
```

---

### 실행 흐름 예시
- 큐: `['A']` → 꺼내서 방문 → 인접 노드 `B, C` 추가  
- 큐: `['B', 'C']` → `B` 방문 → 인접 노드 `D, E` 추가  
- 큐: `['C', 'D', 'E']` → `C` 방문 → 인접 노드 `F` 추가  
- … 이런 식으로 **가까운 노드부터 차례대로** 탐색합니다.

---------------------------------
### 3. Binary Search
- 1920 수 찾기 (실버4)
- 10816 숫자 카드2 (실버4)
- 2417 정수 제곱근 (실버4)
- 6236 용돈관리 (실버1)
- 8983 사냥꾼 (골드4)
- 2110 공유기 설치 (골드4)

---------------------------------
### 4. 스택 & Queue
- 2504 괄호의 값 (골드5)
- 1662 압축(골드4)
- 17608 막대기(브론즈2)
- 3986 좋은 단어 (실버4)
- 2841 외계인의 기타 연주 (실버1)
- 2493 탑(골드5)
- 17298 오큰수 (골드4)
- 9935 문자열 폭발(골드4)
- 1158 요세푸스 문제(실버4)
- 1966 프린터 큐(실버3)
- 5464 주차장 (실버2)
- 3078 좋은 친구(골드4)
