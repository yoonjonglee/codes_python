
def find_pivo(a):

	if(a <= 2):
		return 1
	else:
		return find_pivo(a-2) + find_pivo(a-1)
		
Nth=input("enter number:_ ")

print(find_pivo(int(Nth)))