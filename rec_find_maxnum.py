def rec_fmax(a, len_a):
	#print(len_a)
	if len_a <= 1:
		return a[0]
	else:
		max_num = rec_fmax(a, len_a-1)
		if max_num > a[len_a-1]:
			return max_num
		else:
			return a[len_a-1]

arr = [1,2,3,4,5,69,8,7,6]
#print(len(arr))
print(rec_fmax(arr, len(arr)))