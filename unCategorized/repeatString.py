#repeatString.py

s = 'abbac'
list = ['','']
while 1:
    flag = False
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            list[0] = s[:i]
            list[1] = s[i+2:]
            flag = True
    s = list[0]+list[1]
    if flag ==False :
        break
print(len(s))

list = ['a','b','c','d','d','c','b']
stack = []

for i in range(len(list)):
    if not stack or stack[-1] != list[i]:
        stack.append(list[i])
    elif stack and stack[-1]==list[i]:
        stack.pop()
print(len(stack))