# Welcome to the Python coding playground.
# Generate Roman numerals from a given list of numbers.

# Sample list to use:
numbers = [1, 23, 44, 59, 69, 1111, 127, 999]
"""
900 + 90 + 9 = (1000-100) + (100-10) + (10-1)
127 = 100 + 20 + 7 = 100 + 20 + (5+2)
1111 = 1000 + 100 + 10 + 1
69 = 60 + 9 = 50 + 10 + 5 + (5 - 1)
59 = 50 + 9 = 50 + (10-1)
44 = 40 + 4 = (50 - 10) + (5 - 1)
23 = 20 + 3
숫자 결합 규칙
#  I:1, V:5, X:10, L:50, C:100, D:500, M:1000

덧셈:같거나 작은 값의 기호가 큰 기호 뒤에 오면 두 기호의 값을 더합니다.
예: VI (5+1=6 5 더하기 1은 6), LVIII (50+5+1+1+1=58. 50 더하기 5 더하기1더하기1더하기1은 58)

뺄셈: 작은 값의 기호가 큰 기호 앞에 오면 큰 값에서 작은 값을 뺍니다.
예: IV (5−1=4 5에서 1을 빼면 4), IX (10−1=9 10에서 1을 빼면 9)

반복: 일반적으로 기호는 연속으로 세 번만 반복될 수 있습니다
예: III = 3, 숫자 4 의 경우, IIII 대신 IV가 사용.

뺄셈 예외: I, X, C(1,10,100)만 뺄셈에 사용 가능. V, L, D(5,50,500)는 뺄셈에 사용불가.
기호는 그보다 큰 두 값에서만 뺄 수 있습니다
예: XC는 90 으로 쓸 수 있지만, IC는 99으로 쓸 수 없음
"""
# Type your code here:
def roman(ns):
    rn = [1000, 500, 100, 50, 10, 5, 1]
    for x in ns:
        v = []
        for y in rn:
            q = x // y
            v.append(q)
            x = x - (y * q)
        #print(v)
        res = []
        for i in range(len(v)):
            if i == 0 and v[i] < 4:
                res.append("M"*v[i]) # 1000
            elif i == 1:
                res.append("D"*v[i]) # 500
            elif i == 2:
                if v[i] < 4: res.append("C"*v[i]) # 100
                elif v[i] == 4 and v[i-1] == 1: res.remove("D"); res.append("CM") # 400~
                else: res.append("CD") # 400
            elif i == 3:
                res.append("L"*v[i]) # 50
            elif i == 4:
                if v[i] < 4: res.append("X"*v[i]) # 10
                elif v[i] == 4 and v[i-1] == 1: res.remove("L"); res.append("XC") # 40~
                else: res.append("XL") # 40
            elif i == 5:
                res.append("V"*v[i]) # 5
            elif i == 6:
                if v[i] < 4: res.append("I"*v[i]) # 1
                elif v[i] == 4 and v[i-1] == 1: res.remove("V"); res.append("IX") # 4~
                else: res.append("IV") # 4
        print("".join(res))
"""
[0, 0, 0, 0, 0, 0, 1] 1 : I
[0, 0, 0, 0, 2, 0, 3] 23 : XXIII
[0, 0, 0, 0, 4, 0, 4] 44 : XLIV
[0, 0, 0, 1, 0, 1, 4] 59 : LIX
[0, 0, 0, 1, 1, 1, 4] 69 : LXIX
[1, 0, 1, 0, 1, 0, 1] 1111 : MCXI
[0, 0, 1, 0, 2, 1, 2] 127 : CXXVII
[0, 1, 4, 1, 4, 1, 4] 999 : CMXCIX
"""
"""
other solutions:
def roman(ns):
    roman_mapping = {
        1000: "M", 
        900: "CM", 
        500: "D", 
        400: "CD", 
        100: "C", 
        90: "XC", 
        50: "L", 
        40: "XL", 
        10: "X", 
        9: "IX", 
        5: "V", 
        4: "IV", 
        1: "I"
    }
    
    for number in ns:
        result = ""
        
        for value in roman_mapping.keys():
            while number >= value:
                result += roman_mapping[value]
                number -= value
        
        print(result)
"""
roman(numbers)