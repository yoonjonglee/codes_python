
def rec_gcd(a, b):
	if(b==0):
		return a
	else:
		return rec_gcd(b, a%b)

print(rec_gcd(4, 8))
print(rec_gcd(60, 24))
print(rec_gcd(35, 14))
print(rec_gcd(27, 99))