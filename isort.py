def isort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while 0 <= j and key < a[j]:
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key

d = [4, 1, 3, 2, 5]
isort(d)
print(d)
