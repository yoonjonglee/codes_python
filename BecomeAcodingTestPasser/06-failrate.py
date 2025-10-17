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
    #print(N, STGS_LST)
    
    return N, STGS_LST

# solution function
def solution(N, STGS_LST):
    challengers = [0] * (N + 2)  # 스테이지 번호는 1~N+1, 0은 사용안함
    for stage in STGS_LST:
        challengers[stage] += 1 # 각 스테이지에 도달한 사용자 수 카운트
    
    fail_rates = {} # 스테이지별 실패율 저장
    total = len(STGS_LST) # 전체 사용자 수

    for i in range(1, N + 1):
        if challengers[i] == 0: fail_rates[i] = 0 # 해당 스테이지에 도달한 사용자가 없으면 실패율 0
        else:
            fail_rates[i] = challengers[i] / total # 실패율 계산
            total -= challengers[i] # 다음 스테이지로 넘어갈 때 도달한 사용자 수에서 현재 스테이지에 도달한 사용자 수를 뺌

    # 실패율을 기준으로 스테이지 번호 정렬, 실패율이 같으면 작은 번호가 먼저 오도록 함
    OUT = sorted(fail_rates, key=lambda x: fail_rates[x], reverse=True) # 내림차순 정렬

    return OUT

# run function
N, STGS_LST = inputs()
OUT = solution(N, STGS_LST)

#show result
print(OUT)
