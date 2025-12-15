
def find_pivo(a):
  if a <= 1: return a
  else:
    return find_pivo(a-2) + find_pivo(a-1)
		
Nth=input("enter number:_ ")

print(find_pivo(int(Nth)))

"""
fivo(6)
  - fivo(4)
    - fivo(2)
      - fivo(0)=0
	    - +fivo(1)=1
    - +fivo(3)
      - fivo(1)=1
	    - +fivo(2)
	      - fivo(0)=0
	      - +fivo(1)=1
  - +fivo(5)
    - fivo(3)
      - fivo(1)=1
	    - +fivo(2)
	      - fivo(0)=0
	      - +fivo(1)=1
    - +fivo(4)
      - fivo(2)
	      - fivo(0)=0
	      - +fivo(1)=1
	  - +fivo(3)
	    - fivo(1)=1
	    - +fivo(2)
	      - fivo(0)=0
	      - +fivo(1)=1
"""