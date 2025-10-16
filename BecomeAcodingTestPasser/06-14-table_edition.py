import sys

# input
inputs = sys.stdin.readline
n, k = map(int, inputs().split())
# 8 2
cmd = list(map(str.strip, inputs().split(",")))
# D 2, C, U 3, C, D 4, C, U 2, Z, Z
# ['D 2', 'C', 'U 3', 'C', 'D 4', 'C', 'U 2', 'Z', 'Z']
sol = -1

# code here
def solve(n, k, cmd):
    table  = ["O"] * n # O: not deleted, X: deleted
    deleted = [] # stack of deleted row indices
    cur = k # current cursor position
    for c in cmd:
        if c[0] == "D": # down
            x = int(c.split()[1]) # number of moves
            for _ in range(x):
                cur += 1 # move down
                while cur < n and table[cur] == "X":
                    cur += 1 # skip deleted rows
        elif c[0] == "U": # up
            x = int(c.split()[1]) # number of moves
            for _ in range(x):
                cur -= 1 #
                while cur >= 0 and table[cur] == "X":
                    cur -= 1 # skip deleted rows
        elif c[0] == "C": # delete
            table[cur] = "X" # mark as deleted
            deleted.append(cur) # add to deleted stack
            # move cursor
            next_cur = cur + 1 # try to move down first
            while next_cur < n and table[next_cur] == "X":
                next_cur += 1 # skip deleted rows
            if next_cur < n: # can move down
                cur = next_cur # move down  
            else: # can't move down, move up
                prev_cur = cur - 1 # try to move up
                while prev_cur >= 0 and table[prev_cur] == "X":
                    prev_cur -= 1 # skip deleted rows
                cur = prev_cur # move up
        elif c[0] == "Z": # recover
            if deleted: # if there is any deleted row
                recover = deleted.pop() # get the last deleted row
                table[recover] = "O" # mark as not deleted

    return "".join(table)

sol = solve(n, k, cmd)

# output
print(sol)