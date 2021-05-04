# 9012.py
# 스택 stack
import sys
from typing import List

sys.stdin = open('input/9012')

def my(s:str)->str:
    stack = []
    for p in s:
        if p=='(':
            stack.append(p)
        else :
            if stack:
                stack.pop()
            else :
                return 'NO'
    if not stack:
        return 'YES'
    else:
        return 'NO'

TC = int(input())
for test_case in range(1, TC + 1):
    n =int(sys.stdin.readline().rstrip())
    for _ in range(n):
        print(my(sys.stdin.readline().rstrip()))
