from collections import Counter

#p=["leo", "kiki", "eden"]; c=["eden", "kiki"] #"leo"
#p=["marina", "josipa", "nikola", "vinko", "filipa"]; c=["josipa", "filipa", "marina", "nikola"] #"vinko"
p=["mislav", "stanko", "mislav", "ana"]; c=["stanko", "ana", "mislav"]	#"mislav"


def solution(p, c):
    answer = ''
    dp = Counter(p)
    for x in c:
        dp[x]-=1
    res=sorted(dp.items(), key=lambda item:item[1], reverse=True)
    answer=res[0][0]
    return answer

solution(p, c)