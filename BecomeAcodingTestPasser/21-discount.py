from collections import Counter
want=["banana", "apple", "rice", "pork", "pot"]; number=[3, 2, 2, 2, 1]; discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
#want=["apple"]; number=[10]; discount=["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

def solution(want, number, discount):
    answer = 0; dw = {}; dd=10; cnt=0; #d10s=[]
    for x in range(len(want)): dw[want[x]] = number[x] # dic of want & numbers
    #sdw=sorted(dw.items()); print(sdw) # useless 
    #print(dw); print()
    for y in range(len(discount)):
        if (y + dd) < len(discount): d10=Counter(discount[y:y+dd])
        else: d10=Counter(discount[y:])
        #print(d10)
        #d10s.append(d10) #useless
        #sd10=sorted(d10.items()); sd10s.append(sd10) #useless
        if dw == d10: cnt+=1
        # in dictionary, "==" operator, it returns True if every key-value pairs same, returns False if there is any key-value pair is not same.
        # example: dic1={"a":1, "b":2, "o":3} ; dic2={"b":2, "o":3, "a":1}; print(dic1 == dic2) # True
    #for z in range(len(d10s)): print(d10s[z]) # useless
    answer=cnt
    return answer

print(solution(want, number, discount))