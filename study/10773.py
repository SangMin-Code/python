# 10773.py
# 스택

import sys
from typing import List


sys.stdin = open('input/10773')

stack = []
def my(num:int):
    if num==0 and stack:
        stack.pop()
    else:
        stack.append(num)

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    for _ in range(n):
        my(int(sys.stdin.readline().rstrip()))
    print(sum(stack))