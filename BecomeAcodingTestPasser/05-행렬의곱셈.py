import sys

"""
correct answer
https://school.programmers.co.kr/learn/courses/30/lessons/12949
"""

#input argument
def inputs():
    input = sys.stdin.readline
    col_1st = int(input())
    list2d_1st = [list(map(int, input().split())) for _ in range(col_1st)]
    #print(f"col: {col}")
    #print(f"list2d: {list2d}")
    col_2nd = int(input())
    list2d_2nd = [list(map(int, input().split())) for _ in range(col_2nd)]
    return list2d_1st, list2d_2nd

# solution function
"""
11, 12, 13    11, 12
21, 22, 23    21, 22
              31, 32

11*11 + 12*21 + 13*31, 11*12 + 12*22 + 13*32 
21*11 + 22*21 + 23*31, 21*12 + 22*22 + 23*32
=>
00*00 + 01*10 + 02*20, 00*01 + 01*11 + 02*21 
10*00 + 11*10 + 12*20, 10*01 + 11*11 + 12*21
"""
def  solution(list2d_1st, list2d_2nd):
    
    out = [ [0]*len(list2d_2nd[0]) for _ in range(len(list2d_1st)) ]
    
    for i in range(len(list2d_1st)):
        #0 1
        for j in range(len(list2d_2nd[0])):
            #0 1 
            for k in range(len(list2d_1st[0])):
                #0 1 2
                out[i][j] = out[i][j] + list2d_1st[i][k] * list2d_2nd[k][j]
                #00*00 + 01*10 + 02*20
                
                
    return out
        
       

# run function
list2d_1st, list2d_2nd = inputs()
results = solution(list2d_1st, list2d_2nd)

#show result

print(results)
