
def find_max(arr_num):
	max_num = arr_num[0]
	for i in range(0, len(arr_num)-1):
		#print(i)
		if max_num <= arr_num[i+1]:
			max_num = arr_num[i+1]
			
	print("max number is ")
	return max_num

arr_num=[2,34,4,6,8,12,3,3999,5,7,9]
print(find_max(arr_num))