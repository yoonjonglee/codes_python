# finding the least number of stations to install for covering all in the list
# N : number of apts (len(list)), 0< N <= 200000000
# W : distance of wave, 0 < W <= 10000
# stations : list of number of apt the station installed, ascending sorted, size < 10000, st[x] <= N

n = 11; sts = [4, 11]; w = 1 # 3
#n = 16; sts = [9]; w = 2     # 3

#E.X of 1st input. [0][1][2!][3*][4!][5][6][7][8][9!][10*] 
# -> to cover 0, 1 & 5, 6, 7, 8 zone, 3 stations are needed more. 

def solution(n, sts, w):
    answer = 0
    cnt = 0; lo = 1; i = 0 # 탐색위치는 1부터(lo), i=설치된 기지국 인덱스
    # 전체 아파트 갯수(길이) n 중 현재 탐색위치 부터 탐색
    while lo <= n:
        # 아직 탐색하지 않은 설치 기지국이 남았고, 현재 위치가 현재 기지국 왼쪽 범위 경계 이상 인경우
        if i < len(sts) and lo >= sts[i] - w:
            # 다음 탐색 위치는 현재 기지국 위치 + 전파범위 + 1 
            lo = sts[i] + w + 1
            # 그 다음 탐색 설치 기지국 인덱스 
            i+=1
        else:
            # 현재 위치에 기지국이 설치 되지 않은 경우
            lo += 2*w + 1
            # 현재 위치 lo + w 에 기지국을 설치하고, 그 다음 위치로 이동(양쪽 전파범위: 2*w)
            cnt+=1
            # 설치 했으니 cnt 1 증가
    answer = cnt
    print(answer)
    return answer
    
solution(n, sts, w)