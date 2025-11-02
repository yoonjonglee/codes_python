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
    apt = [0] * n ; cnt = 0
    for x in sts:
        apt[x-1] = 1
        for y in range(1, w+1):
            if (x-1)+(y) <= n-1:
                apt[(x-1)+(y)] = 1
            if (x-1)-(y) >= 0:
                apt[(x-1)-(y)] = 1
    # apt : [0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1]
    # apt : [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    print(apt)
    for z in range(n):
        if apt[z] == 0 and z < n-w:
            apt[z] = 1
            for j in range(1, w+1):
                #if apt[z+(j)] != 1 and z+(j) <= n-1:
                if z+j <= n-1:
                    apt[z+j] = 1
            cnt += 1
    print(apt)
    print(cnt)
    answer = cnt
    return answer
    
solution(n, sts, w)