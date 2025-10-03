import sys

"""
correct answer
#https://school.programmers.co.kr/learn/courses/30/lessons/42840
"""

#input argument
input = sys.stdin.readline
arg = list(map(int, input().split()))

# solution function
def  solution(arg):
    patterns = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0]*3

    for i, answer in enumerate(arg):
        # length of arg
        
        for j, pattern in enumerate(patterns):
            #0:[0..5], 1:[0..8], 2:[0..10]
            if answer == pattern[ i%len(pattern)]:
                # arg:10, patt: 5,
                # 0, 1, 2, 3, 4, / 5[0], 6[1], 7[2] ... ...
                scores[j] = scores[j] + 1
                
    return scores

# run function
results = solution(arg)

#find the max
scores_max = max(results)

#show result
sorts=[]
for i in range(len(results)):
    if scores_max == results[i]:
        sorts.append(i)

print(sorted(sorts))
