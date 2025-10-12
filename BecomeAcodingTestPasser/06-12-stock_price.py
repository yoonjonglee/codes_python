import sys

# input
prices = list(map(int, input().split()))
'''
example
input : [1, 2, 3, 2, 3]
output : [4, 3, 1, 1, 0]
Explanation:
- len(prices) = 5, history of 5 seconds
- prices[0] = 1, in the next 4 seconds, the price is always >= 1, so prices[0] = 4
- prices[1] = 2, in the next 3 seconds, the price is always >= 2, so prices[1] = 3
- prices[2] = 3, in the next 2 seconds, the price drops to 2 at the 4th second, so prices[2] = 1
- prices[3] = 2, in the next 1 second, the price is always >= 2, so prices[3] = 1
- prices[4] = 3, there are no next seconds, so prices[4] = 0
# Write a code that transforms the input list 'prices' into the output list as described above.
'''

# code here

undrop_times = []
for i in range(len(prices)):
    cnt = 0
    for j in range(i + 1, len(prices)):
        cnt += 1 # Count every second until the end
        if prices[i] > prices[j]: break # Stop counting if the price drops

    undrop_times.append(cnt)

"""
여기서 문제는 가격이 떨어졌을 때도 cnt를 세지 않는다는 점이에요.
문제의 조건은 "가격이 떨어지는 순간까지의 시간"을 세야 하는데,
지금 코드는 떨어진 순간을 카운트하지 않고 그냥 건너뛰어버립니다.
예를 들어 prices = [3, 2]일 때:
- i=0에서 3을 기준으로 보면, 바로 다음에 2로 떨어지죠.
- 정답은 [1, 0]이어야 하는데, 지금 코드에서는 cnt=0이 되어 [0, 0]이 나옵니다.
즉, 떨어지는 순간도 1초로 세야 하는데, 그걸 빼먹은 것이 핵심 오류예요.
"""

# output
print(undrop_times)

"""
⚡ 스택 풀이 (쉽게 설명)
스택 풀이가 처음 보면 어렵게 느껴지는데, 사실은 **"가격이 떨어지는 순간을 바로 처리"**하는 방식이에요.
아이디어
- i번째 시점의 가격이 떨어지는 순간을 만나면, 그때 바로 i의 답을 확정해버립니다.
- 아직 떨어지지 않은 시점들은 스택에 넣어두고, 나중에 처리합니다.
- 스택에는 (인덱스, 가격) 쌍을 넣어두고, 새로운 가격이 들어올 때마다 스택의 맨 위와 비교합니다.

def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []  # 아직 가격이 안 떨어진 시점들을 저장

    for i, price in enumerate(prices):
        # 스택에 있는 것들 중에서 현재 가격보다 높은 것들은 "떨어진 것"
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            answer[j] = i - j  # 떨어진 시점까지 걸린 시간
        stack.append(i)

    # 끝까지 안 떨어진 것들은 마지막까지 유지
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j

    return answer

🔎 동작 예시 ([1, 2, 3, 2, 3])
- i=0, price=1 → 스택=[0]
- i=1, price=2 → 스택=[0,1]
- i=2, price=3 → 스택=[0,1,2]
- i=3, price=2 → 3>2이므로 2번 꺼내고 answer[2]=3-2=1
→ 스택=[0,1,3]
- i=4, price=3 → 스택=[0,1,3,4]
끝까지 돌고 나면 스택에 남은 것들 처리:
- answer[0]=4, answer[1]=3, answer[3]=1, answer[4]=0
최종 결과: [4, 3, 1, 1, 0]
"""