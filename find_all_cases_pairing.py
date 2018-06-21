
def find_all_cases_pairing(a):
    n = len(a)
    #print(str(n))

    for i in range(0,n):
        for j in range(i+1,n):
            if a[i] != a[j]:
                print(a[i] +"-"+ a[j])
    return

#name = ["Tom", "Jerry", "Mike"]
name = ["Dony", "Raphy", "Leo", "Mikey"]
print(find_all_cases_pairing(name))
