from collections import Counter

# https://school.programmers.co.kr/learn/courses/30/lessons/131127
#  회원등록시 정현이가 원하는 제품을 모두 할인 받을 수 있는 회원등록 날짜의 총 일수를 return 하는 solution 함수를 완성하시오. 가능한 날이 없으면 0을 return 합니다.

want=["banana", "apple", "rice", "pork", "pot"]; number=[3, 2, 2, 2, 1]; discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
#want=["apple"]; number=[10]; discount=["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

def solution(want, number, discount):
    answer = 0; dw = {}; dd=10; cnt=0 # dd is the discount days
    for x in range(len(want)): dw[want[x]] = number[x] # O(N), dw is the dictionary of want & numbers
    for y in range(len(discount)):
        if (y + dd) < len(discount): d10=Counter(discount[y:y+dd]) # O(10), d10 is the dictionary of discount, if the discount days is less than the length of the discount, then the discount days is the length of the discount from the current day
        else: d10=Counter(discount[y:]) # O(10), d10 is the dictionary of discount, if the discount days is greater than the length of the discount, then the discount days is the length of the discount
        if dw == d10: cnt+=1 # O(1)
        # in dictionary, "==" operator, it returns True if every key-value pairs same, returns False if there is any key-value pair is not same.
        # example: dic1={"a":1, "b":2, "o":3} ; dic2={"b":2, "o":3, "a":1}; print(dic1 == dic2) # True
    answer=cnt
    return answer

print(solution(want, number, discount))