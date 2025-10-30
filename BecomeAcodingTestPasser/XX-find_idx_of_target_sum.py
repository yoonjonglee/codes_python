# Welcome to the Python coding playground.
# Find which two numbers of the given numbers list, when summed up, equal the target value. Return their indices.

# Sample list and target values to use:
numbers = [1, 2, 4, 7, 12]
target1 = 6 # 1, 2
target2 = 11 # 2, 3
target3 = 18 # 2, 4, 12

# Type your code here:
def find_indices_of_target_sum(ns, t):
    """
    for x in range(len(ns)):
        if ns[x] > t: continue
        elif (t-ns[x]) in ns: return x, ns.index(t-ns[x])
    """
    """
    idx = {}
    for x, n in enumerate(ns):
        cv = t - n
        if cv in idx: return idx[cv], x
        idx[n] = x; print(idx)
    """
    res = []
    for x in range(len(ns)):
        ct = t
        for y in range(x, len(ns)):
            ct = ct - ns[y]
            #print(ct)
            if ct in 

    

#print(find_indices_of_target_sum(numbers, target1))  # (1, 2)
#print(find_indices_of_target_sum(numbers, target2))  # (2, 3)
print(find_indices_of_target_sum(numbers, target3))