from collections import Counter

#orders=["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]; course=[2,3,4]   #["AC", "ACDE", "BCFG", "CDE"]
orders=["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]; course=[2,3,5] #["ACD", "AD", "ADE", "CD", "XYZ"]
#orders=["XYZ", "XWY", "WXA"]; course=[2,3,4] #["WX", "XY"]
#course의 각 number는 guest가 주문 시, "number"개 이상 포함되어 주문 된 것이어야 함. 예) A, B 모두 총 주문이 2회로 같아도, 2개 단품에 포함된 메뉴를 선택 

def solution(orders, course):
    answer = []; so=""
    for x in orders: so+=x
    dms=Counter(list(so)) #sorted(list(set(so)))
    print(dms)


    return answer

print(solution(orders, course))