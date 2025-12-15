#answer(explain) each items.

#1.1
text="hi"; print(text.center(10))
#1.2
text="hi"; print(text.center(10, '-'))
#1.3
t=[[1], [1,2], [1,2,3]]; print(t[-1])
#1.4
t=[[1], [1,2], [1,2,3]]; print(list(map(str, t[-1])))
#1.5
t=[[1], [1,2], [1,2,3]]; print(len(" ".join(map(str, t[-1]))))
#1.6
t=[[1], [1,2], [1,2,3]]; t.append([1,2,3,4]); print(t)
#1.7
p1 = [5, 8]; p2 = [3, 6]; abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
#1.8
import itertools; from itertools import permutations, combinations
#1.9
permutations('ABC', 2) #('A','B'),('A','C'),('B','A'),('B','C'),('C','A'),('C','B')
#1.10
combinations('ABC', 2) #('A','B'),('A','C'),('B','C')
#2.1
l = [[10, 19], [7, 10], [6, 10]]; print(sorted(l, key=lambda item:item[1]))
#2.2
l = [[10, 19], [7, 10], [6, 10]]; print(sorted(l, key=lambda item:item[1], reverse=True))
#2.3
d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}; print(d.items())
#2.4
d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}; print(dict(sorted(d.items())))
#2.5 
d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}; print(list(sorted(d.items())))
#2.6 
d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}; print(dict(sorted(d.items(), key=lambda item:item[1])))
#2.7 
d = {'A':[10, 19], 'B':[7, 10], 'C':[6, 10]}; print(dict(sorted(d.items(), key=lambda item:item[1][1])))
#2.8
arr=[5, 2, 0, 9, 0, 1, 0, 5, 0, 6]; nz=0; for i in range(len(arr)): if arr[i]!=0: arr[nz]=arr[i]; nz+=1; for j in range(nz, len(arr)): arr[j]=0
#3.1
dic={}; for n in range(3): dic[n]=str(n); print(dic)
#3.2
dic={1:2,2:1,3:1}; for n in dic.keys(): print(dic.get(n))
#3.3
ns=[1,1,2,3]; dic={}; for n in ns: dic[n]=dic.get(n,0)+1; print(dic)
#3.4
dic={1:2,2:1,3:1}; print(max(dic,key=dic.get))
#3.5
from collections import Counter
#3.6
ts = [1,3,2,5,4,5,2,3]; print(Counter(ts))
#4.1
def factorial(n): if n == 1: return 1"\n" return n*factorial(n-1)
#4.2
def sum_list(li): if not li: return 0 "\n" return li[0]+sum_list(li[1:])
#4.3
def fibonacci(n): if n<=1 return n "\n" return fibonacci(n-2)+fibonacci(n-1)
#4.4
def preorder(nodes, idx):
  if idx < len(nodes):
    ret = str(nodes[idx]) + " "; ret += preorder(nodes, idx * 2 + 1); ret += preorder(nodes, idx * 2 + 2)
    return ret
  else: return ""
print(preorder([1, 2, 3, 4, 5, 6, 7], 0)[:-1]) # "1 2 4 5 3 6 7"
4.5
def inorder(nodes, idx):
  if idx < len(nodes):
    ret = inorder(nodes, idx * 2 + 1); ret += str(nodes[idx]) + " "; ret += inorder(nodes, idx * 2 + 2)
    return ret
  else: return ""
print(inorder([1, 2, 3, 4, 5, 6, 7], 0)[:-1]) # "4 2 5 1 6 3 7
#4.6
def postorder(nodes, idx):
  if idx < len(nodes):
    ret = postorder(nodes, idx * 2 + 1); ret += postorder(nodes, idx * 2 + 2); ret += str(nodes[idx]) + " "
    return ret
  else: return ""
print(postorder([1, 2, 3, 4, 5, 6, 7], 0)[:-1]) # "4 5 2 6 7 3 1"