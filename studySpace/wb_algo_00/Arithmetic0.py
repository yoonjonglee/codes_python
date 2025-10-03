'''

- n개의 정수 중, 홀수 들의 합계
- Arithmetic(등차수열): 연속하는 두 수의 차이가 일정한 수열
- <1> input - n개의 정수
- <2> process-알고리즘
- <3> output

'''

# <1> input - n개의 정수
sum = 0                  # init result variable

# <2> process-알고리즘: 주어진 범위(given range)에 주어진 조건(given condition, 필터링) -> for loop
for i in range(1, 20):            # given range : 1~20
    if i % 2 != 0:           # given condition : odd number
        sum = sum + i        # Arithmetic (algorithm)
        print(i, end=' ')

# <3> output
print(f"정수 1~20 중 홀수의 총합: {sum}")