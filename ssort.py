def sel_sort(d):
    for i in range(len(d)-1):
        print(i)
        #print(d[i])
        for j in range(i+1, len(d)):
            print(j)
            #print(d[j])
            #if (d[i] > d[j]): # sort by min order
            if (d[i] < d[j]): # sort by max order
                #swap 1
                #temp = d[j]
                #d[j] = d[i]
                #d[i] = temp
                #swap 2
                d[j], d[i] = d[i], d[j]

#d = [9, 3, 1, 2, 5]
d = [2, 4, 5, 1, 3]
#print(str(len(d)))
sel_sort(d)
print(d)
