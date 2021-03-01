#parenthesis.py

'''
{{{((()))}}}
'''

s = '{{{((()))}}}'

stack =[]
result = 1
for i in s:
    if i == '{' or i== '(' :
        stack.append(i)
    elif (i=='}' or i ==')') and len(stack)==0 :
        result =0
        break
    elif i == '}':
        if stack.pop() != '{':
            result = 0
            break
    elif i == ')':
        if stack.pop() != '(':
            result = 0
            break
if len(stack)!=0 :
    result =0
print(result)