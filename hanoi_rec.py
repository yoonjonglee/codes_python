

def hanoi(n, col_start, col_end, col_trans):
	if(n==1):
		print(str(col_start) +"->"+ str(col_end))
		return
	else:
		hanoi(n-1, col_start, col_trans, col_end)
		print(str(col_start) +"->"+ str(col_end))
		hanoi(n-1, col_trans, col_end, col_start)
		
		
#hanoi(1, 1, 3, 2)
#hanoi(3, 1, 3, 2)
#hanoi(4, 1, 3, 2)
hanoi(2, 1, 3, 2)