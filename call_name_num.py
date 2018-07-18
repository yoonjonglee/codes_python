def call_name_num(list_num, list_name, num):
    len_num = len(list_num)
    len_name = len(list_name)

    if len_num == len_name:
        for i in range(len_num):
            if num == list_num[i]:
                return list_name[i]
        return "?"
    else:
        print("list sizes are different")
        return

    num = int(num)
    temp = []
    for i in range(n):
        #print(list[i])
        #print(num)
        if num == int(list[i]):
            temp.append(i)
    return temp

stu_num = [4, 5, 6, 7]
stu_name = ["rose", "ronaldo", "umtiti", "young"]
print(call_name_num(stu_num, stu_name, 8))
print(call_name_num(stu_num, stu_name, 7))
print(call_name_num(stu_num, stu_name, 6))
print(call_name_num(stu_num, stu_name, 5))
print(call_name_num(stu_num, stu_name, 4))


