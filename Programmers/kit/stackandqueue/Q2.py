# Q1.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(priorities:List[int],location:int)->int:

    queue = collections.deque()
    for i,j in enumerate(priorities):
        queue.append([i,j])

    priorities.sort()
    answer = 0
    while queue:
        if queue[0][1]==priorities[-1]:
            answer+=1
            if queue[0][0]==location:
                return answer
            else:
                queue.popleft()
                priorities.pop()
        else:
            queue.append(queue.popleft())
    return -1

TC = int(input())
for test_case in range(1, TC + 1):
    priorities = list(map(int,input().split()))
    location = int(input())
    answer = my(priorities,location)
    print(answer)
