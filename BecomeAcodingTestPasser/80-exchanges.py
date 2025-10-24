import sys

#amount = 123
amount = 350

# The greedy approach to minimize the number of exchanges
# unit : 1, 10, 50, 100

u = [100, 50, 10, 1]
result = []
for i in u:
    cnt = amount // i
    result.extend([i] * cnt)
    amount = amount % i

print(result)