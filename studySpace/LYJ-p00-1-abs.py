import math


def abs_sign(a):
    if a>0:
        return a
    else:
        return -a


def abs_square(a):
    b = a*a
    return math.sqrt(b)

print(abs_sign(-10))
print(abs_sign(5))
print(abs_sign(-988))

print(abs_square(9))
print(abs_square(-22))
print(abs_square(-7))

"""
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