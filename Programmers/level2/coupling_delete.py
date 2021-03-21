#coupling_delete.py
#programmers.co.kr/learn/courses/30/lessons/12973
import sys
sys.stdin=open('input/coupling_delete')
from typing import List

def my(s:str)->int:
    stack = [s[0]]
    for i in s[1:]:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    if stack :
        return 0
    else :
        return 1

def pracitce(s:str)->int:
    stack = [s[0]]
    for i in s[1:]:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    return 0 if stack else 1


TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    answer = my(s)
    print(answer)