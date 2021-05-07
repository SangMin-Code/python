# 15828.py
import sys
from typing import List

sys.stdin = open('input/15828')
import collections

def my(size:int, inputs:List[int])->List[int]:
    queue = collections.deque(maxlen=size)
    for i in inputs:
        if i==0:
            queue.popleft()
        elif len(queue)==size:
            pass
        else :
            queue.append(i)
    return list(queue)


TC = int(input())
for test_case in range(1, TC + 1):
    size= int(sys.stdin.readline().rstrip())
    inputs =[]
    while True:
        i = int(sys.stdin.readline().rstrip())
        if i ==-1:
            break
        inputs.append(i)
    answer = my(size,inputs)
    if not answer:
        print('empty')
    else :
        for i in answer:
            print(i)
