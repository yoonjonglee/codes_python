import sys

def input():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]

    return N, info

#input
sol = -1
N, info = input()
'''
https://miscellaneous-house.blogspot.com/2025/10/python-algo-copilot.html

in case of 3, 7 --> in this case, upside down
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1
0 0 1 1 1 1 1 1 1 1
0 0 1 1 1 1 1 1 1 1
0 0 1 1 1 1 1 1 1 1
'''

#code here

def get_edge(paper):
    edge = 0
    d = ((0, -1), (0, 1), (-1, 0), (1, 0)) #left, right, up, down
    for r in range(100):
        for c in range(100):
            if paper[r][c] == 1:
                for dc, dr in d:
                    nc, nr = c+dc, r+dr
                    if (not 0<=nc<100) or (not 0<=nr<100) or paper[nr][nc] == 0: edge += 1
    return edge

def putting_paper(paper, info):
    for sc, sr in info:
        for r in range(sr, sr+10):
            for c in range(sc, sc+10):
                paper[r][c] = 1

def solve(info):
    paper = [[0]*100 for _ in range(100)]
    putting_paper(paper, info)
    return get_edge(paper)

sol = solve(info)

#output
print(sol)