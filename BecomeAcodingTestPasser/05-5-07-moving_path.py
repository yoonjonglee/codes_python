import sys



# input
input = sys.stdin.readline
'''
exmaple input
ULURRDLLU, LULLLLLLU. ...

expected output
7, 7, ...
'''
sol = -1
#code here
#dir = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
current = [0, 0]
hist = set()

def solve(path):
    #cnt = 0
    for i in path:
        if i == 'U' and current[1] < 5:
            hist.add(tuple(current))
            current[1] += 1
        elif i == 'D' and current[1] > -5:
            hist.add(tuple(current))
            current[1] -= 1
        elif i == 'R' and current[0] < 5:
            hist.add(tuple(current))
            current[0] += 1
        elif i == 'L' and current[0] > -5:
            hist.add(tuple(current))
            current[0] -= 1

        print(i, current, hist)

    return len(hist)

dir_list = list(input())
sol = solve(dir_list)

#output
print(sol)


# correct answer: 7
'''
https://school.programmers.co.kr/learn/courses/30/lessons/49994?language=python3

좋은 질문이에요. 지금 작성하신 코드가 실패하는 이유는 **문제의 요구사항과 저장 방식이 어긋나 있기 때문**이에요. 핵심은 **“방문한 좌표의 개수”가 아니라 “방문한 길(간선)의 개수”**를 세야 한다는 점입니다.

---

### 🔎 현재 코드의 문제점
1. **hist에 저장하는 값**
   - 지금은 `hist.add(tuple(current))`로 **현재 위치(노드)**만 저장하고 있어요.
   - 하지만 문제에서 요구하는 건 "처음 지나가는 길(간선)"의 개수예요.  
     즉, `(출발 좌표, 도착 좌표)` 쌍을 저장해야 합니다.

2. **양방향 고려 필요**
   - 예를 들어 `(0,0) → (0,1)`로 이동한 길과 `(0,1) → (0,0)`로 이동한 길은 같은 길로 취급해야 합니다.
   - 따라서 `(start, end)`와 `(end, start)`를 모두 같은 길로 간주해야 해요.

3. **현재 코드의 결과**
   - 단순히 좌표만 저장하므로, 같은 좌표를 여러 번 방문하면 중복이 제거되어 길의 개수가 잘못 계산됩니다.
   - 예: `"UD"` → (0,0) → (0,1) → (0,0)  
     실제로는 같은 길을 두 번 지나므로 답은 1이어야 하는데, 지금 코드에서는 `{(0,0),(0,1)}`가 저장되어 2가 됩니다.

---

### ✅ 수정 아이디어
- 이동할 때마다 **출발 좌표와 도착 좌표를 묶어서 저장**해야 합니다.
- 예:  
  ```python
  start = tuple(current)
  current[1] += 1   # 이동
  end = tuple(current)
  hist.add((start, end))
  hist.add((end, start))  # 양방향 동일 처리
  ```

---

### ✨ 올바른 코드 구조 예시
```python
def solution(path):
    current = [0, 0]
    hist = set()

    for i in path:
        start = tuple(current)
        if i == 'U' and current[1] < 5:
            current[1] += 1
        elif i == 'D' and current[1] > -5:
            current[1] -= 1
        elif i == 'R' and current[0] < 5:
            current[0] += 1
        elif i == 'L' and current[0] > -5:
            current[0] -= 1
        else:
            continue  # 범위 밖이면 무시

        end = tuple(current)
        hist.add((start, end))
        hist.add((end, start))  # 같은 길로 취급

    return len(hist) // 2  # 양방향 저장했으니 절반만 카운트
```

---

👉 정리하면, 실패 이유는 **좌표만 저장해서 "길"이 아니라 "방문한 점"을 세고 있었기 때문**이에요.  
이제 `간선(길)`을 저장하도록 바꾸면 모든 테스트 케이스에서 통과할 수 있습니다.

'''