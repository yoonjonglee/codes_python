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