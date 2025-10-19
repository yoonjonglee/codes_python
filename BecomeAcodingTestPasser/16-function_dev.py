import sys
from collections import deque
import math

inputs = sys.stdin.readline

prog = list(map(int, inputs().split()))
spd = list(map(int, inputs().split()))

# code here
"""
prog = [93, 30, 55]
spd = [1, 30, 5]
f1: days to be relased,  100-93=7/1=7 -> 7 
f2: days to be relaesed, 100-30=70/30=2.33 -> 3
f3: days to be relaesed, 100-55=45/5=9 -> 9 
relase order: f1, f2, f3
if the value of next f is less than or equal to the current f, it will be released (poped) together.
"""
def solve(prog, spd):
    days = [] # days to be released
    for p, s in zip(prog, spd): 
        day = (100 - p) / s # days needed to complete the feature
        # with import math.ceil
        day = math.ceil(day)
        # without import math
        #if day != int(day): day = int(day) + 1
        #else: day = int(day)
        days.append(day) # append days to be released

    q = deque(days) # use deque for efficient popping from the front
    result = [] # result list to store the number of features released together
    while q: # while there are still features to be released
        rel = q.popleft() # current feature's release day
        cnt = 1 # count of features released together
        while q and rel >= q[0]: # check the next feature's release day
            cnt += 1 # increment count
            q.popleft() # pop the next feature as it's released together
        result.append(cnt) # append the count to the result list

    return result

sol = solve(prog, spd)

# output
print(sol)

"""
좋은 질문이에요! 파이썬의 **`zip()` 함수**는 여러 개의 **iterable(리스트, 튜플, 문자열 등)** 을 동시에 묶어서 병렬 처리할 수 있게 해주는 아주 유용한 내장 함수입니다.  

---

## 🧩 기본 개념
- `zip()`은 같은 인덱스에 있는 요소들을 **튜플**로 묶어줍니다.
- 결과는 **zip 객체**로 반환되며, 보통 `list()`나 `tuple()`로 감싸서 확인합니다.
- 가장 짧은 iterable의 길이에 맞춰서 동작합니다.

---

## 📌 기본 사용법
```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

zipped = zip(a, b)
print(list(zipped))  
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

## 📌 길이가 다를 때
```python
a = [1, 2, 3, 4]
b = ['x', 'y']

print(list(zip(a, b)))
# [(1, 'x'), (2, 'y')]   # 짧은 쪽(b)에 맞춰서 멈춤
```

---

## 📌 여러 개 묶기
```python
a = [1, 2, 3]
b = ['a', 'b', 'c']
c = ['🍎', '🍌', '🍇']

print(list(zip(a, b, c)))
# [(1, 'a', '🍎'), (2, 'b', '🍌'), (3, 'c', '🍇')]
```

---

## 📌 언패킹(unzip) 활용
`zip()`을 반대로 풀 때는 `*` 연산자를 사용합니다.
```python
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, chars = zip(*pairs)

print(nums)   # (1, 2, 3)
print(chars)  # ('a', 'b', 'c')
```

---

## ✅ 활용 예시
- 두 리스트를 **딕셔너리**로 만들기
```python
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Seoul']

my_dict = dict(zip(keys, values))
print(my_dict)
# {'name': 'Alice', 'age': 25, 'city': 'Seoul'}
```

- 반복문에서 동시에 순회하기
```python
names = ['Tom', 'Jane', 'Mike']
scores = [90, 85, 77]

for name, score in zip(names, scores):
    print(f"{name}의 점수는 {score}점")
```

---

👉 정리하면, `zip()`은 **여러 시퀀스를 병렬로 묶어서 처리할 때** 아주 강력한 도구예요.  
혹시 원하시면, `zip()`과 비슷하지만 길이가 다를 때도 맞춰주는 `itertools.zip_longest`도 같이 설명해드릴까요?

"""