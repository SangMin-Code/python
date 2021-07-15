# Q1.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(prgress:List[int],speeds:List[int])->List[int]:
    answer = []
    queue = collections.deque()
    for i in range(len(prgress)):
        queue.append([prgress[i],speeds[i]])
    while queue:
        temp =0
        while queue and queue[0][0]>=100:
            temp+=1
            queue.popleft()
        if temp>0:
            answer.append(temp)
        for i in range(len(queue)):
                queue[i][0]=queue[i][0]+queue[i][1]
    return answer

def my2(progress:List[int],speeds:List[int])->List[int]:
    answer = []
    time, count = 0,0
    while len(progress)>0:
        if(progress[0]+time*speeds[0])>=100:
            progress.pop(0)
            speeds.pop(0)
            count+=1
        else:
            if count>0:
                answer.append(count)
                count=0
            time+=1
    answer.append(count)
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    progress = list(map(int,input().split()))
    speeds = list(map(int,input().split()))
    answer = my(progress,speeds)
    print(answer)
