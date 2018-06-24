def fact(num):
    val = 1
    for x in range(1,num+1):
        val = val * x
    return val

num = input("input number: ")
result = fact(int(num))
print(result)


