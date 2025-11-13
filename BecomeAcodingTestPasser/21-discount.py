from collections import Counter
want=["banana", "apple", "rice", "pork", "pot"]; number=[3, 2, 2, 2, 1]; discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
#want=["apple"]; number=[10]; discount=["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]

def solution(want, number, discount):
    answer = 0; dw = {}; dd=10; d10s=[]
    for x in range(len(want)): dw[want[x]] = number[x] # dic of want & numbers
    #sdw=sorted(dw.items())
    #print(sdw)
    print(dw)
    print()
    for y in range(len(discount)):
        if (y + dd) < len(discount):
            d10=Counter(discount[y:y+dd])
        else:
            d10=Counter(discount[y:])
        #print(d10)
        #sd10=sorted(d10.items())
        #sd10s.append(sd10)
        d10s.append(d10)
    #print(d10s)
    for z in range(len(d10s)):
        print(d10s[z])
    #for y in range(len(discount)):
        #if (discount[y] in dw) and (dw[discount[y]] > 0):
            #dw[discount[y]] -= 1
            #dd -= 1

    

    return answer

solution(want, number, discount)