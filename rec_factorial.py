
def rec_factorial(n):
    #print(n)
	if n <= 1:
	    return 1
	else:
	    return n * rec_factorial(n-1)

num = input("input number: ")
print(rec_factorial(int(num)))