# 2164.py
# queue 큐
import sys
from typing import List

sys.stdin = open('input/2164')
import collections

def my(N:int):
    #가장 밑의 값을 빼서 가장 위로 올리기, 가장 밑의 값을 빼기를 반복
    queue = collections.deque([i+1 for i in range(N)])
    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]

TC = int(input())
for test_case in range(1, TC + 1):
    N=int(sys.stdin.readline().rstrip())
    answer = my(N)
    print(answer)
