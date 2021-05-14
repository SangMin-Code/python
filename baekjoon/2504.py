# 2504.py
import sys
from typing import List

sys.stdin = open('input/2504')


def my(s:str)->int:
    stack = []

    for i in s:
        if i==")":
            temp =0
            while stack:
                top = stack.pop()
                if top =="(":
                    if temp==0:
                        stack.append(2)
                    else :
                        stack.append(2*temp)
                    break
                elif top=="[":
                    return 0
                else:
                    if temp==0:
                        temp =int(top)
                    else :
                        temp = temp+int(top)
        elif i=="]":
            temp =0
            while stack:
                top = stack.pop()
                if top=="[":
                    if temp==0:
                        stack.append(3)
                    else:
                        stack.append(3*temp)
                    break
                elif top=="(":
                    return 0
                else :
                    if temp==0:
                        temp=int(top)
                    else :
                        temp = temp+int(top)
        else :
            stack.append(i)

    if "(" in stack or "[" in stack:
        return 0
    return sum(stack)






TC = int(input())
for test_case in range(1, TC + 1):
    s=sys.stdin.readline().rstrip()
    answer = my(s)
    print(answer)
