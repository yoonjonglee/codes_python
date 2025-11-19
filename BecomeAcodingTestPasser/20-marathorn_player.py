from collections import Counter

# https://school.programmers.co.kr/learn/courses/30/lessons/42576?language=python3

#p=["leo", "kiki", "eden"]; c=["eden", "kiki"] #"leo"
#p=["marina", "josipa", "nikola", "vinko", "filipa"]; c=["josipa", "filipa", "marina", "nikola"] #"vinko"
p=["mislav", "stanko", "mislav", "ana"]; c=["stanko", "ana", "mislav"]	#"mislav"


def solution(p, c):
    answer = '' # answer is the name of the player who did not finish the marathon
    dp = Counter(p) # dp is a dictionary of the list
    for x in c:
        dp[x]-=1 # dp[x] is the number of the player who did not finish the marathon
    res=sorted(dp.items(), key=lambda item:item[1], reverse=True) 
    # res is a list of the dictionary, sorted by the value in descending order
    answer=res[0][0] 
    # answer is the name of the player who did not finish the marathon. 
    # because the list is sorted by the value in descending order, 
    # the first element is the name of the player who did not finish the marathon
    return answer

solution(p, c)