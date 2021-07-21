# Q3.py
import sys
from typing import List

sys.stdin = open('input/Q3')


def my(number:str, k:int)->str:
    stack = []

    for i in range(len(number)):
        if stack:
            while stack and stack[-1]<number[i] and k>0:
                stack.pop()
                k-=1
            stack.append(number[i])
        else:
            stack.append(number[i])

    return ''.join(list(map(str,stack[:len(stack)-k])))

TC = int(input())
for test_case in range(1, TC + 1):
    number,k = map(str,input().split())
    answer = my(number,int(k))
    print(answer)
