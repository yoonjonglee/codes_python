from collections import Counter
import itertools

#orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]; course=[2,3,4]   #["AC", "ACDE", "BCFG", "CDE"]
#orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]; course=[2,3,5] #["ACD", "AD", "ADE", "CD", "XYZ"]
orders=["XYZ", "XWY", "WXA"]; course=[2,3,4] #["WX", "XY"]
#course의 각 number는 guest가 주문 시, "number"개 이상 포함되어 주문 된 것이어야 함. 예) 2인 경우, 여러 메뉴 조합 중 2개 조합 A, C 의 경우, A, C가 모두 각 손님 주문 이력에 포함 되어있어야 함.

# Worse Answer - Out of the time limitation due to the use of permutations.
"""
def solution(orders, course):
    answer = []; so=""
    for x in orders: so+=x
    lo=[list(s) for s in orders]; #print(lo)
    sms=sorted(list(set(so))); #print(sms)
    for co in course:
        psms=list(dict.fromkeys(itertools.permutations(sms, co))); lpsms = []
        for x in range(len(psms)):
            for y in range(len(lo)):
                if all(z in lo[y] for z in psms[x]):
                    lpsms.append(psms[x])
        dlpsms=Counter(lpsms)
        fdlpsms = [[k, v] for k, v in dlpsms.items() if v == max(dlpsms.values()) and v>=2]
        lfdlpsms = [l[0] for l in fdlpsms]
        out = list({tuple(sorted(p)) for p in lfdlpsms})
        res = ["".join(r) for r in out]
        for it in res: answer.append(it)

    return sorted(answer)
"""
# Better Answer - use of Combinations
def solution(orders, course):
    answer = []
    for co in course:
        csms = []
        for ord in orders:
            comb=itertools.combinations(sorted(ord), co)
            csms+=comb
        print([list(cb) for cb in csms])

    return sorted(answer)

print(solution(orders, course))

"""
#================================================================
itertools.permutations()는 중복 원소가 있을 경우 동일한 순열을 여러 번 생성합니다. 이를 제거하려면 set()을 사용하거나, 더 효율적으로는 itertools.permutations 대신 itertools.permutations 결과를 dict.fromkeys()로 중복 제거할 수 있습니다.
itertools.permutations() generates the same permutation multiple times if there are duplicate elements. To remove them, use set() , or more efficiently, remove duplicates from the itertools.permutations result by calling dict.fromkeys() instead of itertools.permutations .
#================================================================
예시: 총 8개 중 2가지 Permutation 계산 = 8*7=56, 3가지 계산 = 8*7*6=336, 5가지 계산 = 8*7*6*5*4=6720
#================================================================
`combinations`와 `permutations`는 모두 **itertools** 모듈에서 제공하는 조합 관련 함수이지만, 두 함수의 핵심 차이는 **순서의 고려 여부**입니다.

- **`combinations(iterable, r)`**  
  - 순서를 **고려하지 않고** r개의 원소를 뽑습니다.  
  - 예: `combinations('ABC', 2)` → `('A', 'B')`, `('A', 'C')`, `('B', 'C')`  
  - 즉, `'AB'`와 `'BA'`는 같은 조합으로 취급됩니다.

- **`permutations(iterable, r)`**  
  - 순서를 **고려하여** r개의 원소를 뽑습니다.  
  - 예: `permutations('ABC', 2)` → `('A', 'B')`, `('A', 'C')`, `('B', 'A')`, `('B', 'C')`, `('C', 'A')`, `('C', 'B')`  
  - `'AB'`와 `'BA'`는 서로 다른 경우로 취급됩니다.

요약하자면,  
- **combinations** → 순서 무시, 중복 없음  
- **permutations** → 순서 고려, 가능한 모든 순열 생성
"""