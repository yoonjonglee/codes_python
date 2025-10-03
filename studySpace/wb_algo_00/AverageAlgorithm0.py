'''
- Average algorithm: 주어진 범위에 주어진 조건에 해당하는 자료들의 평균
- Ex> n명의 정수 중, 80점이상, 95점 이하의 자료들의 평균
- <1> input - n개의 정수
- <2> process-알고리즘
- <3> output

'''

# <1> input - n명의 성적
data = [90, 65, 78, 50, 95]
AVG = 0         # init output variable, AVG = SUM/CNT          
SUM = 0         # init output variable
CNT = 0         # init output variable           
LEN = len(data) # init output variable, length of data[]

# <2> process-알고리즘: 주어진 범위(given range)에 주어진 조건(given condition, 필터링) -> for loop
for i in range(0, LEN):            # given range : length of [data]
    if (data[i] >= 80) and (data[i] <= 95):   # given condition : 80<=i<=95
        SUM = SUM + data[i]                   # add every num filtered
        CNT = CNT + 1

if SUM != 0 and CNT != 0:
    AVG = SUM / CNT
else:
    print("No such conditioned numbers")

# <3> output
print(f"80점이상, 95점 이하의 자료들의 평균: {AVG:.2f}")
