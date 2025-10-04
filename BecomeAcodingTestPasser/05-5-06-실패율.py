import sys

"""
correct answer
https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3

FR : 해당 스테이지 못꺤 사용자 수 / 해당 스테이지 도달 또는 클리어 사용자 수
N : 스테이지 갯수
STGS[] : 전체 사용자들의 현재 스테이지 번호 리스트, 즉 len(STGS) 는 전체 사용자 수, 
- 1 ~ N+1까지 스테이지 번호 존재, N+1은 전체N개 스테이지들을 다 클리어 했음을 의미
OUT[] : 실패율이 높은 스테이지 번호들 부터 내림차순으로 정렬
- 실패율이 같은 스테이지 번호는 작은 번호가 먼저
- 사용자가 없는 스테이지 번호는 실패율을 0으로 간주

N = 5
STGS_LST = [2, 1, 2, 6, 2, 4, 3, 3]
USRS = len(STGS)
STGS_SET = list(set(STGS_LST))
"""

#input argument

def inputs():
    input = sys.stdin.readline
    N = int(input())
    STGS_LST = list(map(int, input().split()))
    print(N, STGS_LST)
    
    return N, STGS_LST

# solution function
def solutions(N, STGS_LST):
    STGS_SET_LST = list(set(STGS_LST)) # remove duplicate stage numbers
    print(STGS_SET_LST)
    OUT_LST = []
    #OUT_DIC = {}
    #for i in STGS_SET_LST: # #12345 ...
    for i in range(1, N+1):
        #12345
        NUMS_STGS_STY_CLR = 0
        NUMS_STGS_STY_UNCLR = 0
        for j in STGS_LST:
            #2, 1, 2, 6, 2, 4, 3, 3
            if i in STGS_SET_LST and  i <= j : NUMS_STGS_STY_CLR += 1
            if i in STGS_SET_LST and i == j: NUMS_STGS_STY_UNCLR += 1
        print(f"stage{i}'s NUMS_STGS_STY_CLR: {NUMS_STGS_STY_CLR}")
        print(f"stage{i}'s NUMS_STGS_STY_UNCLR: {NUMS_STGS_STY_UNCLR}")
        
        if NUMS_STGS_STY_CLR != 0:
            FR = NUMS_STGS_STY_UNCLR / NUMS_STGS_STY_CLR
        else:
            FR = 0        
        #OUT_DIC[i] = FR
        OUT_LST.append((i, FR))

    #OUT_DIC_DESC = sorted(OUT_DIC.items(), key= lambda item:item[1], reverse=True)
    #OUT_DIC_DESC = dict(sorted(OUT_DIC.items(), key= lambda item:item[1], reverse=True))    
    #print(OUT_DIC_DESC)
    OUT_LST_DESC = sorted(OUT_LST, key= lambda x: x[1], reverse=True)
    
    #OUT = list(OUT_DIC_DESC.keys())
    OUT = [x[0] for x in OUT_LST_DESC]
    
    return OUT

# run function
N, STGS_LST = inputs()
OUT = solutions(N, STGS_LST)

#show result
print(OUT)

'''
좋은 질문이에요 👍  
이 코드가 **시간초과**가 나는 핵심 이유는 바로 **중첩 반복문** 때문이에요. 쉽게 풀어서 설명해볼게요.

---

## 🚨 문제의 원인
```python
for i in range(1, N+1):       # 스테이지 개수만큼 반복 (최대 N번)
    for j in STGS_LST:        # 사용자 수만큼 반복 (최대 len(STGS_LST)번)
```

- 즉, **N × len(STGS_LST)** 만큼 반복이 일어나요.  
- 예를 들어, N=500, STGS_LST 길이가 200,000이라면 → **1억 번 이상 연산**이 발생합니다.  
- 프로그래머스 같은 코딩테스트 환경에서는 보통 1억 번 연산은 시간초과가 나기 쉽습니다.

---

## 🔎 세부적으로 비효율적인 부분
1. `if i in STGS_SET_LST`  
   - 이 조건을 매번 검사하는데, 사실 `range(1, N+1)`을 돌고 있으니 필요 없는 조건이에요.  
   - 어차피 모든 스테이지를 다 계산해야 하니까 `in` 체크는 불필요합니다.

2. `for j in STGS_LST` 안에서 매번 `i <= j`, `i == j` 비교  
   - 결국 같은 리스트를 계속 처음부터 끝까지 훑고 있어요.  
   - 이게 시간복잡도를 폭발적으로 키우는 원인입니다.

---

## ✅ 효율적인 접근 방법
실패율 문제의 핵심은 **각 스테이지에 도달한 사람 수**와 **그 스테이지에서 멈춘 사람 수**를 빠르게 구하는 거예요.  
이를 위해 **한 번만 STGS_LST를 순회**해서 카운트를 세우면 됩니다.

### 방법
1. `Counter` 또는 배열을 이용해 **각 스테이지에 멈춘 사람 수**를 미리 구한다.
2. 전체 사용자 수에서 차례대로 빼면서 **도달한 사람 수**를 구한다.
3. 실패율 계산은 O(N)만에 끝난다.

---

## 📝 정리
- 현재 코드는 **스테이지 수 × 사용자 수** 만큼 불필요하게 반복 → 시간초과 발생.
- 해결책은 **STGS_LST를 한 번만 순회해서 카운트**를 만든 뒤, 누적해서 도달 인원을 계산하는 방식으로 바꾸는 것.

---

원한다면 제가 이 코드를 **시간초과 안 나게 최적화된 버전**으로 다시 짜드릴 수도 있어요.  
바로 고쳐드릴까요, 아니면 먼저 제가 설명한 원리를 코드로 직접 적용해보시겠어요?

'''