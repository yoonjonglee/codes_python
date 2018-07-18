def num_search(list, num):
    n = len(list)
    num = int(num)
    temp = []
    for i in range(n):
        #print(list[i])
        #print(num)
        if num == int(list[i]):
            temp.append(i)
    return temp

list = [4, 5, 6, 7, 78, 998, 12, 7]
print(num_search(list, 7))
print(num_search(list, 12))
print(num_search(list, 666))

