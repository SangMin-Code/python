# 18258.py
# queue 큐
import sys
from typing import List
import collections
sys.stdin = open('input/18258')


queue = collections.deque()
def my(s:str):
    command = s.split()
    if command[0] == 'push':
         queue.append(command[1])
    elif command[0] == 'pop':
        if not queue:
            print(-1)
        else :
            print(queue.popleft())
    elif command[0] =='size':
            print(len(queue))
    elif command[0] =='empty':
        if not queue:
            print(1)
        else :
            print(0)
    elif command[0] =='front':
        if not queue:
            print(-1)
        else :
            print(queue[0])
    elif command[0] =='back':
        if not queue:
            print(-1)
        else :
            print(queue[-1])
n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    my(sys.stdin.readline().rstrip())
