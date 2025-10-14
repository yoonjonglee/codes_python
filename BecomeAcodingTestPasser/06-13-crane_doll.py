import sys

def input_data():
    readl = sys.stdin.readline
    B = int(readl())
    board = [list(map(int,readl().split())) for _ in range(B)]
    moves = list(map(int, readl().split()))
    return B, board, moves

# input
b, board, moves = input_data()
'''
b = 5

board =
0 0 0 0 0
0 0 1 0 3
0 2 5 0 1
4 2 4 4 2
3 5 1 3 1

moves =
1 5 3 5 1 2 1 4

basket =
4:4
1:X
2:2
1:3(X)
5:1(X)
3:1(X)
5:3(X)
1:4
--> (left dolls)
4
2
4
sol = 4 # of dolls removed
'''
# code here
def solve(board, moves):
    basket = [] # stack
    sol = -1
    for mv in moves:
        for r in range(len(board)):
            if board[r][mv-1] != 0: # found a doll
                doll = board[r][mv-1]
                board[r][mv-1] = 0 # remove the doll from the board
                if len(basket) > 0 and basket[-1] == doll:
                    basket.pop() # remove the top doll
                    #nonlocal sol
                    sol += 2 # two dolls removed (exloded)
                else:
                    basket.append(doll) # add the doll to the basket
                break # move to the next move

    return sol

sol = solve(board, moves)

# output
print(sol)