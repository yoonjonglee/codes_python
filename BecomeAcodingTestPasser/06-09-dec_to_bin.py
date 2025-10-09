import sys

#input argument
inputs = sys.stdin.readline

n = inputs().strip()
sol = -1

#code here
'''
the simpleast way to convert decimal to binary in Python is to use the built-in bin() function.

def dec_to_bin(n):
    return bin(int(n))[2:]  # 0b 제거
sol = dec_to_bin(n)
'''
def dec_to_bin(n):
    if n == '0': return '0'
    n = int(n)
    bin = []
    while n > 0 :
        bin.append(str(n % 2))
        n = n // 2
    
    #return ''.join(reversed(bin)) # reversed() 함수 사용 - way1
    binary = ''
    while bin: binary += bin.pop() # pop() 함수 사용 - way2

    return binary

sol = dec_to_bin(n)

# output
#print(str(sol)) 
print(sol)