import sys
#input
#b = 9
#rq = [1,3,2,5,4]
b = 10
rq = [2,2,3,3]

#code here
cb = b; cnt = 0 # current budget
rq.sort(); print(rq) # 1,2,3,4,5 or 2,2,3,3 : sort requests ascending
for i in rq:
    if i > cb: break # can't afford to support this request amount
    cb -= i # approve budget request
    cnt += 1 # count approved requests
if cb < 0: cnt -= 1 # if over budget, decrease count by 1s
#output
print(cnt)