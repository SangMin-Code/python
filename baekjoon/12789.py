# 12789.py
import collections
import sys
from typing import List

sys.stdin = open('input/12789')

def my(n:int, students:List[int])->str:
    stack = []
    queue = collections.deque(students)
    num =0

    while queue:
        stack.append(queue.popleft())
        while queue and queue[0]==num+1:
            num = queue.popleft()
        while stack and stack[-1]==num+1:
            num = stack.pop()
    if stack:
        return 'Sad'
    else :
        return 'Nice'

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    students = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(n,students)
    print(answer)
