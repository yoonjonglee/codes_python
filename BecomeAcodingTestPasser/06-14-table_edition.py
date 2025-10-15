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
    table  = ["O"] * n
    deleted = []
    cur = k
    for c in cmd:
        if c[0] == "D":
            x = int(c.split()[1])
            for _ in range(x):
                cur += 1
                while cur < n and table[cur] == "X":
                    cur += 1
        elif c[0] == "U":
            x = int(c.split()[1])
            for _ in range(x):
                cur -= 1
                while cur >= 0 and table[cur] == "X":
                    cur -= 1
        elif c[0] == "C":
            table[cur] = "X"
            deleted.append(cur)
            # move cursor
            next_cur = cur + 1
            while next_cur < n and table[next_cur] == "X":
                next_cur += 1
            if next_cur < n:
                cur = next_cur
            else:
                prev_cur = cur - 1
                while prev_cur >= 0 and table[prev_cur] == "X":
                    prev_cur -= 1
                cur = prev_cur
        elif c[0] == "Z":
            if deleted:
                recover = deleted.pop()
                table[recover] = "O"

    return table

sol = solve(n, k, cmd)

# output
print(sol)