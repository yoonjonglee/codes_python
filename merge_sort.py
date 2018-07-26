
def msort(a):
    n = len(a)
    if(n<=1):
        return
    else:
        mid = n//2
        g1 = a[:mid]
        #print(g1)
        msort(g1)
        g2 = a[mid:]
        #print(g2)
        msort(g2)
        i1=0
        i2=0
        ia=0
        while i1 < len(g1) and i2 < len(g2):
            if g1[i1] < g2[i2]:
                a[ia] = g1[i1]
                ia = ia + 1
                i1 = i1 + 1
            else:
                a[ia] = g2[i2]
                ia = ia + 1
                i2 = i2 + 1
        while i1 < len(g1):
            a[ia] = g1[i1]
            ia = ia + 1
            i1 = i1 + 1
        while i2 < len(g2):
            a[ia] = g2[i2]
            ia = ia + 1
            i2 = i2 + 1


d=[8, 6, 5, 7, 3, 2, 9, 1]
msort(d)
print(d)
