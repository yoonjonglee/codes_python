import sys

"""
correct answer
#https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""

#input argument
input = sys.stdin.readline
arg = list(map(int, input().split()))

# solution function
def  solution(arg):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0]*3

    for i, answer in enumerate(arg):
        # length of arg
        
        for j, pattern in enumerate(patterns):
            #0:[0..5], 1:[0..8], 2:[0..10]
            if answer == pattern[ i%len(pattern)]:
                # arg:10, patt: 5,
                # 0, 1, 2, 3, 4, / 5[0], 6[1], 7[2] ... ...
                scores[j] = scores[j] + 1
                
    return scores

# run function
results = solution(arg)

#find the max
scores_max = max(results)

#show result
sorts=[]
for i in range(len(results)):
    if scores_max == results[i]:
        sorts.append(i)

print(sorted(sorts))

"""
`enumerate()`는 **리스트나 문자열 같은 반복 가능한 객체를 순회할 때,**  
각 요소의 **인덱스(번호)**와 **값**을 **같이** 꺼내주는 파이썬 내장 함수예요.

쉽게 말하면,  
`for`문에서 `i`(번호)와 `value`(값)를 동시에 얻고 싶을 때 쓰는 도우미입니다.

---

### 예시
```python
fruits = ["apple", "banana", "cherry"]

for idx, fruit in enumerate(fruits):
    print(idx, fruit)
```

**출력**
```
0 apple
1 banana
2 cherry
```

---

### 특징
- 기본 인덱스는 **0**부터 시작하지만, `enumerate(리스트, start=1)`처럼 시작 번호를 바꿀 수 있어요.
- 코드가 깔끔해지고, `range(len(...))`를 쓰는 것보다 가독성이 좋습니다.

---

원하면 제가 `enumerate()`를 쓰는 경우와 안 쓰는 경우를 비교해서 보여드릴까요?  
그렇게 하면 차이가 더 잘 보입니다.
"""