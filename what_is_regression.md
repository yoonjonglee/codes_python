**재귀 함수는 자기 자신을 다시 호출하는 함수로, 반복문 대신 문제를 단계적으로 쪼개 해결할 때 유용합니다.** 예를 들어 팩토리얼이나 피보나치 수열 계산 같은 문제에서 자주 쓰입니다.

---

## 🧩 재귀 함수 기본 개념
- **정의**: 함수 안에서 자기 자신을 다시 호출하는 함수.
- **구조**:
  1. **기본 조건(Base case)**: 더 이상 재귀 호출을 하지 않고 종료하는 조건.
  2. **재귀 호출(Recursive case)**: 문제를 더 작은 단위로 나누어 자기 자신을 호출.

---

## 📌 간단한 예시들

### 1. 팩토리얼 계산
```python
def factorial(n):
    if n == 1:  # 기본 조건
        return 1
    return n * factorial(n - 1)  # 재귀 호출

print(factorial(5))  # 결과: 120
```
- `factorial(5)` → `5 * factorial(4)` → … → `1`까지 내려가며 계산.

---

### 2. 피보나치 수열
```python
def fibonacci(n):
    if n <= 1:  # 기본 조건
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 결과: 8
```
- `fibonacci(6)`은 `fibonacci(5) + fibonacci(4)`로 계속 분해.

👍 피보나치 수열 코드를 아주 쉽게 풀어서 설명해볼게요.
---

## 🌀 피보나치 수열이란?
- 앞의 두 수를 더해서 다음 수를 만드는 규칙.
- 시작은 보통 `0, 1` → 그 다음은 `1, 2, 3, 5, 8, 13 …`

---

## 📌 코드 구조 다시 보기
```python
def fibonacci(n):
    if n <= 1:  # 기본 조건
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))  # 결과: 8
```

### 1. `if n <= 1: return n`
- `n`이 0이나 1이면 그냥 그 값을 반환.
- 즉, **시작점(0, 1)**을 직접 알려주는 부분.

### 2. `return fibonacci(n - 1) + fibonacci(n - 2)`
- 그 외에는 **앞의 두 수를 더해서 결과를 만든다**는 규칙을 코드로 표현.
- `fibonacci(n)`을 구하려면 `fibonacci(n-1)`과 `fibonacci(n-2)`를 다시 계산.

---

## 🔎 `fibonacci(6)` 계산 과정 따라가기
1. `fibonacci(6)` → `fibonacci(5) + fibonacci(4)`
2. `fibonacci(5)` → `fibonacci(4) + fibonacci(3)`
3. `fibonacci(4)` → `fibonacci(3) + fibonacci(2)`
4. 계속 쪼개다 보면 결국 `fibonacci(1)`과 `fibonacci(0)`까지 내려감.
   - `fibonacci(1)` = 1  
   - `fibonacci(0)` = 0  

이 값들을 하나씩 더해 올라오면서 최종적으로 `8`이 됨.

---

## 🧮 계산 흐름 간단히 정리
```
fibonacci(6)
= fibonacci(5) + fibonacci(4)
= (fibonacci(4) + fibonacci(3)) + (fibonacci(3) + fibonacci(2))
= ...
= 8
```

---

## ✅ 핵심 포인트
- **재귀 함수는 큰 문제를 작은 문제로 쪼개서 해결**한다.
- 피보나치에서는 "앞의 두 수를 더한다"는 규칙을 계속 반복.
- 결국 `0`과 `1`이라는 **기본 조건**까지 내려가서 다시 합쳐 올라온다.

---
**트리 그림**으로 `fibonacci(6)`이 어떻게 분해되는지 시각적으로 보여줄 수도 있어요.
```
fibonacci(6)
├─ fibonacci(5)
│  ├─ fibonacci(4)
│  │  ├─ fibonacci(3)
│  │  │  ├─ fibonacci(2)
│  │  │  │  ├─ fibonacci(1) → 1
│  │  │  │  └─ fibonacci(0) → 0
│  │  │  └─ fibonacci(1) → 1
│  │  └─ fibonacci(2)
│  │     ├─ fibonacci(1) → 1
│  │     └─ fibonacci(0) → 0
│  └─ fibonacci(3)
│     ├─ fibonacci(2)
│     │  ├─ fibonacci(1) → 1
│     │  └─ fibonacci(0) → 0
│     └─ fibonacci(1) → 1
└─ fibonacci(4)
   ├─ fibonacci(3)
   │  ├─ fibonacci(2)
   │  │  ├─ fibonacci(1) → 1
   │  │  └─ fibonacci(0) → 0
   │  └─ fibonacci(1) → 1
   └─ fibonacci(2)
      ├─ fibonacci(1) → 1
      └─ fibonacci(0) → 0
```

---

### 3. 리스트 합 구하기
```python
def list_sum(lst):
    if not lst:  # 빈 리스트면 0 반환
        return 0
    return lst[0] + list_sum(lst[1:])

print(list_sum([1, 2, 3, 4]))  # 결과: 10
```
- 리스트를 하나씩 줄여가며 합을 계산.

---

## ⚠️ 주의할 점
- **무한 재귀 방지**: 반드시 종료 조건(Base case)을 설정해야 함.
- **성능 문제**: 재귀는 함수 호출이 많아져 속도가 느려질 수 있음 → 반복문이나 메모이제이션으로 최적화 가능.
- **가독성 장점**: 복잡한 문제를 간단하고 직관적으로 표현 가능.

---

## ✅ 정리
- **재귀 함수는 "큰 문제를 작은 문제로 쪼개서 자기 자신을 호출"하는 방식**이다.  
- **팩토리얼, 피보나치, 리스트 처리** 같은 문제에서 자주 활용된다.  
- **종료 조건을 반드시 넣어야 안전하게 동작**한다.  

혹시 원한다면 제가 **재귀와 반복문을 비교하는 표**도 만들어 드릴까요?
