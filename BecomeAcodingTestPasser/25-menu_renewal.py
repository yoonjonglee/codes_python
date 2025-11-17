from collections import Counter
import itertools

orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]; course=[2,3,4]   #["AC", "ACDE", "BCFG", "CDE"]
#orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]; course=[2,3,5] #["ACD", "AD", "ADE", "CD", "XYZ"]
#orders=["XYZ", "XWY", "WXA"]; course=[2,3,4] #["WX", "XY"]
#course의 각 number는 guest가 주문 시, "number"개 이상 포함되어 주문 된 것이어야 함. 예) A, B 모두 총 주문이 2회로 같아도, 2개 단품에 포함된 메뉴를 선택 

def solution(orders, course):
    answer = []; so=""
    for x in orders: so+=x
    sms=sorted(list(set(so))); print(sms)
    dms=Counter(list(so)); print(dms)
    """
    itertools.permutations()는 중복 원소가 있을 경우 동일한 순열을 여러 번 생성합니다. 이를 제거하려면 set()을 사용하거나, 더 효율적으로는 itertools.permutations 대신 itertools.permutations 결과를 dict.fromkeys()로 중복 제거할 수 있습니다.
    itertools.permutations() generates the same permutation multiple times if there are duplicate elements. To remove them, use set() , or more efficiently, remove duplicates from the itertools.permutations result by calling dict.fromkeys() instead of itertools.permutations .
    """
    #print(["".join(list(p)) for p in dict.fromkeys(itertools.permutations(sms, 2))]) #8*7=56
    #print(["".join(list(p)) for p in dict.fromkeys(itertools.permutations(sms, 3))]) #8*7*6=336
    #print(["".join(list(p)) for p in dict.fromkeys(itertools.permutations(sms, 5))]) #8*7*6*5*4=6720
    #for x in course:
        #psms=list("".join(dict.fromkeys(itertools.permutations(sms, x))))
    psms=["".join(list(p)) for p in dict.fromkeys(itertools.permutations(sms, 2))]
    for pair in psms:
        for o in orders:
            if pair in o and pair not in answer:
                answer.append(pair)

    return answer

print(solution(orders, course))