def num_search(list, num):
	n = len(list)
	num = int(num)
	for i in range(n):
		#print(list[i])
		#print(num)
		if num == int(list[i]):
			return i

	return -1

list = [4, 5, 6, 7, 78, 998, 12, 7]
print(num_search(list, 6))
print(num_search(list, 78))
print(num_search(list, 2))
print(num_search(list, 7))
