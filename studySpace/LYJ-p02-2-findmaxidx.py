import math

def findmaxidx(a):
    n = len(a)
    max_v = a[0]
    max_v_idx = 0
    for i in range(1, n):
        if (max_v < a[i]):
            max_v = a[i]
            max_v_idx = i
            
    return max_v_idx

v = [9, 2, 8, 1, 3, 4, 5, 7, 6, 87, 64]
w = [10, 22, 33, 11, 9, 1918, 1111111, 2]
x = [112121, 272, 99]
y = [18, 1212, 5957, 29822, 101, 111, 4752]

print(findmaxidx(v))
print(findmaxidx(w))
print(findmaxidx(x))
print(findmaxidx(y))


"""
def findmax(a):
    n = len(a)
    max_v = a[0]
    for i in range(1, n):
        if (max_v < a[i]):
            max_v = a[i]
            
    return max_v

v = [9, 2, 8, 1, 3, 4, 5, 7, 6, 87, 64]
w = [10, 22, 33, 11, 9, 1918, 1111111, 2]
x = [112121, 272, 99]
y = [18, 1212, 5957, 29822, 101, 111, 4752]

print(findmax(v))
print(findmax(w))
print(findmax(x))
print(findmax(y))

def sum(a):
    #result = a*(a+1)/2 #<-- float divide
    result = a*(a+1)//2 #<-- integer divide
    return result
    
def sum(a):
    result = 0
    for i in range(1, a+1):
        result = i + result
        
    return result
    

def abs_sign(a):
    if a>0:
        return a
    else:
        return -a


def abs_square(a):
    b = a*a
    return math.sqrt(b)


words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")


numbers = list(range(10))
print(numbers) #0123456789

numbers = list(range(3, 8))
print(numbers) #34567

numbers = list(range(5, 20, 2))
print(numbers) #5791113 ... 19

x = list(range(7, 3, -1))
print(x) #7654
"""