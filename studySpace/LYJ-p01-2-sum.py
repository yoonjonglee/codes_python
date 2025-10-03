import math

def sum(a):
    #result = a*(a+1)/2 #<-- float divide
    result = a*(a+1)//2 #<-- integer divide
    return result


print(sum(10))
print(sum(100))
print(sum(1000))

"""
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