'''
- Count algorithm: 주어진 범위에 주어진 조건에 해당하는 자료들의 갯수
- Ex> 1부터 1000까지 정수 중, 13의 배수의 갯수(건수, 횟수)
- <1> input - n개의 정수
- <2> process-알고리즘
- <3> output

'''

# <1> input - n개의 정수
count = 0                  # init output variable

# <2> process-알고리즘: 주어진 범위(given range)에 주어진 조건(given condition, 필터링) -> for loop
for i in range(1, 1000):            # given range : 1~1000
    if i % 13 == 0:           # given condition : multiples of 13
        count = count + i        # increase count output num

# <3> output
print(f"1부터 1000까지 정수 중, 13의 배수의 갯수: {count}")