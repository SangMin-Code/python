# 4949.py
# stack 스택
import sys
from typing import List

sys.stdin = open('input/4949')

def my(s:str)->str:
    dic = {")":"(","]":"["}
    stack = []
    for p in s:
        if p =='(' or p=='[':
            stack.append(p)
        elif p ==')' or p=="]":
            if stack:
                if stack[-1] != dic[p]:
                    return "no"
                else :
                    stack.pop()
            else :
                return 'no'
    if stack:
        return 'no'
    else :
        return 'yes'

TC = int(input())
for test_case in range(1, TC + 1):
    s = sys.stdin.readline().rstrip()
    print(my(s))
