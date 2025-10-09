import sys

#input argument
inputs = sys.stdin.readline
ps = inputs()
'''
[](){} 
}]()[{ 
'''
#code here
def chk(ps_list, stack):
    for p in ps_list:
        if p in ['(', '{', '[']:
            stack.append(p)
        elif p in [')', '}', ']']:
            if not stack:
                return 0 # stack is empty
            top = stack.pop()
            if (top == '(' and p != ')') or (top == '{' and p != '}') or (top == '[' and p != ']'):
                return 0 # not matching with top
    if len(stack) == 0: return 1  # all matched
    else: return 0 # still some left in stack

ps_list = list(ps.strip())
stack = []
cnt = 0
for x in ps_list:
    #print(ps_list)
    cnt += chk(ps_list, stack)
    ps_list.append(ps_list[0]) # rotate (left effect)
    ps_list.pop(0) # rotate (right effect)

#output result
print(cnt)