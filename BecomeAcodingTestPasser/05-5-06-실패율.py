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
    STGS_SET_LST = list(set(STGS_LST)) 
    print(STGS_SET_LST)
    #OUT = []
    OUT_DIC = {}
    #for i in STGS_SET_LST: # #12346
    for i in range(1, N+1):
        #12345
        NUMS_STGS_STY_CLR = 0
        NUMS_STGS_STY_UNCLR = 0
        for j in STGS_LST:
            #2, 1, 2, 6, 2, 4, 3, 3
            if i in STGS_SET_LST and  i <= j :
                NUMS_STGS_STY_CLR += 1
            if i in STGS_SET_LST and i == j:
                NUMS_STGS_STY_UNCLR += 1
        print(f"NUMS_STGS_STY_UNCLR: {NUMS_STGS_STY_UNCLR}")
        print(f"NUMS_STGS_STY_CLR: {NUMS_STGS_STY_CLR}")
        if NUMS_STGS_STY_CLR != 0:
            FR = NUMS_STGS_STY_UNCLR / NUMS_STGS_STY_CLR
        else:
            FR = 0        
        OUT_DIC[i] = FR

    #OUT_DIC_DESC = sorted(OUT_DIC.items(), key= lambda item:item[1], reverse=True)
    OUT_DIC_DESC = dict(sorted(OUT_DIC.items(), key= lambda item:item[1], reverse=True))    
    print(OUT_DIC_DESC)
    
    OUT = list(OUT_DIC_DESC.keys())
    
    return OUT

# run function
N, STGS_LST = inputs()
OUT = solutions(N, STGS_LST)

#show result
print(OUT)
