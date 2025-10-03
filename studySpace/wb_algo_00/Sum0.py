'''

- n명의 점수 중, 80점 이상 점수의 합계
- 합계: 주어진 범위에 주어진 조건에 해당하는 자료들의 합
- <1> input - n명의 점수
- <2> process-알고리즘
- <3> output

'''

# <1> input - n명의 점수
scores = [100, 75, 50, 37, 90, 95]
sum = 0                  # init result variable
N = len(scores)          # N명 

# <2> process-알고리즘: 주어진 범위에 주어진 조건(필터링) -> for loop
for i in range(0, N):            # given range
    if scores[i] >= 80:          # given condition
        sum = sum + scores[i]    # sumation (algorithm)

# <3> output
print(f"{N}명의 점수 중 80점 이상의 총점: {sum}")