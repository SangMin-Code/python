# 10828.py
# 스택
import sys
from typing import List
sys.stdin = open('input/10828')

stack = []
def my(s:str):
    command = s.split()
    if command[0] == 'push':
         stack.append(command[1])
    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else :
            print(stack.pop())
    elif command[0] =='size':
            print(len(stack))
    elif command[0] =='empty':
        if not stack:
            print(1)
        else :
            print(0)
    elif command[0] =='top':
        if not stack:
            print(-1)
        else :
            print(stack[-1])

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    my(sys.stdin.readline().rstrip())
