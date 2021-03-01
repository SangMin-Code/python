#calculate.py


#s= '10 2 + 3 4 + * .'

s='5 3 * + .'
exp = list(s.split(' '))

def cal(exp):
    stack = []
    for i in range(len(exp)-1):
        if exp[i].isdecimal():
            stack.append(str(exp[i]))
        else :
            t = []
            for j in range(2):
                if len(stack)==0 :
                    print('error')
                    return
                else :
                    t.append(str(stack.pop()))
            a = t.pop()
            b = t.pop()
            stack.append(eval(b+exp[i]+a))
    result = stack.pop()
    # error 처리 수정
    if result == False or len(stack) !=0 :
        print('error')
        return
    else: print(result)
print('1 ' ,end='')
cal(exp)
