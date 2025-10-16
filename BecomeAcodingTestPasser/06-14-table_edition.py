import sys

# input
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
# 8 2
cmd = list(map(str.strip, inputs().split(",")))
# D 2, C, U 3, C, D 4, C, U 2, Z, Z
# ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z']
sol = -1

# code here
def solve(n, k, cmd):
    table  = ["O"] * n # O: not deleted, X: deleted
    deleted = [] # stack of deleted row indices
    cur = k # current cursor position
    for c in cmd:
        if c[0] == "D": # down
            x = int(c.split()[1]) # number of moves
            for _ in range(x):
                cur += 1 # move down
                while cur < n and table[cur] == "X":
                    cur += 1 # skip deleted rows
        elif c[0] == "U": # up
            x = int(c.split()[1]) # number of moves
            for _ in range(x):
                cur -= 1 #
                while cur >= 0 and table[cur] == "X":
                    cur -= 1 # skip deleted rows
        elif c[0] == "C": # delete
            table[cur] = "X" # mark as deleted
            deleted.append(cur) # add to deleted stack
            # move cursor
            next_cur = cur + 1 # try to move down first
            while next_cur < n and table[next_cur] == "X":
                next_cur += 1 # skip deleted rows
            if next_cur < n: # can move down
                cur = next_cur # move down  
            else: # can't move down, move up
                prev_cur = cur - 1 # try to move up
                while prev_cur >= 0 and table[prev_cur] == "X":
                    prev_cur -= 1 # skip deleted rows
                cur = prev_cur # move up
        elif c[0] == "Z": # recover
            if deleted: # if there is any deleted row
                recover = deleted.pop() # get the last deleted row
                table[recover] = "O" # mark as not deleted

    return "".join(table)

sol = solve(n, k, cmd)

# output
print(sol)

"""
지금 제출한 코드가 **시간 초과**가 나는 이유는,  
`D`, `U`, `C` 명령에서 **삭제된 행을 건너뛰기 위해 while 루프를 매번 돌고 있기 때문**이에요.  

즉, 커서를 한 칸씩 이동하면서 삭제된 행을 건너뛰는 방식은  
최악의 경우 명령 하나당 O(N) 시간이 걸리고, 명령이 M개면 O(N×M)까지 커집니다.  
`n`과 명령 수가 수십만 이상이면 바로 시간 초과가 납니다.

---

## 문제 원인
- 현재 구조:  
  - `table` 리스트로 삭제 여부를 저장 (`O`/`X`)  
  - 이동할 때마다 while로 삭제된 행을 건너뜀 → **매번 선형 탐색**
- 삭제/복구가 많아질수록 건너뛰는 구간이 길어져서 성능이 급격히 나빠짐.

---

## 해결 방법
이 문제는 **양방향 연결 리스트(doubly linked list)** 또는 **prev/next 배열**을 사용하면  
커서 이동이 O(1)에 가능해집니다.  
삭제 시 현재 행을 스택에 저장하고, 복구 시 prev/next 연결을 다시 복원하면 됩니다.

---

### 수정 코드 예시 (prev/next 배열 방식)
```python
import sys
inputs = sys.stdin.readline

n, k = map(int, inputs().split())
cmd = list(map(str.strip, inputs().split(",")))

def solve(n, k, cmd):
    # prev[i] = i의 위 행 번호, next[i] = i의 아래 행 번호
    prev = [i - 1 for i in range(n)] # [-1, 0, 1, 2, 3, 4, 5, 6], n=8
    next = [i + 1 for i in range(n)] # [1, 2, 3, 4, 5, 6, 7, 8], n=8
    prev[0] = -1   # 첫 행은 위가 없음
    next[-1] = -1  # 마지막 행은 아래가 없음

    deleted = []   # 삭제된 행 스택
    cur = k

    for c in cmd:
        if c[0] == "D":
            x = int(c.split()[1])
            for _ in range(x):
                cur = next[cur]
        elif c[0] == "U":
            x = int(c.split()[1])
            for _ in range(x):
                cur = prev[cur]
        elif c[0] == "C":
            deleted.append((cur, prev[cur], next[cur]))
            # 연결 끊기
            if prev[cur] != -1:
                next[prev[cur]] = next[cur]
            if next[cur] != -1:
                prev[next[cur]] = prev[cur]
            # 커서 이동
            cur = next[cur] if next[cur] != -1 else prev[cur]
        elif c[0] == "Z":
            row, p, n_ = deleted.pop()
            if p != -1:
                next[p] = row
            if n_ != -1:
                prev[n_] = row

    # 결과 문자열 만들기
    result = ["O"] * n
    for row, _, _ in deleted:
        result[row] = "X"
    return "".join(result)

print(solve(n, k, cmd))
```

---

### 동작 원리 설명
- **prev/next 배열**: 각 행의 위/아래 행 번호를 저장해 두면, 이동 시 O(1)로 바로 건너뛸 수 있습니다.
- **삭제(C)**: 현재 행을 스택에 `(행번호, 위행, 아래행)` 형태로 저장하고, prev/next 연결을 끊습니다.
- **복구(Z)**: 스택에서 꺼내서 prev/next 연결을 다시 복원합니다.
- **이동(U/D)**: prev 또는 next 배열을 따라가면 삭제된 행을 건너뛰는 과정이 필요 없습니다.

---

이 방식은 모든 명령이 **O(1)**에 처리되므로,  
`n`과 명령 수가 수십만이어도 시간 초과 없이 통과합니다.

---
"""