import sys

# input
prices = list(map(int, input().split()))
'''
example
input : [1, 2, 3, 2, 3]
output : [4, 3, 1, 1, 0]
Explanation:
- len(prices) = 5, history of 5 seconds
- prices[0] = 1, in the next 4 seconds, the price is always >= 1, so prices[0] = 4
- prices[1] = 2, in the next 3 seconds, the price is always >= 2, so prices[1] = 3
- prices[2] = 3, in the next 2 seconds, the price drops to 2 at the 4th second, so prices[2] = 1
- prices[3] = 2, in the next 1 second, the price is always >= 2, so prices[3] = 1
- prices[4] = 3, there are no next seconds, so prices[4] = 0
# Write a code that transforms the input list 'prices' into the output list as described above.
'''

# code here

undrop_times = []
for i in range(len(prices)):
    cnt = 0
    for j in range(i + 1, len(prices)):
        if prices[i] <= prices[j]:
            cnt += 1
        else:
            continue
    undrop_times.append(cnt)

# output
print(undrop_times)