#disk_controller.py
import sys
sys.stdin=open('input/disk_controller')
from typing import List
import heapq


def my(jobs:List[int])->int:
    answer, now, i =0,0,0
    start = -1
    heap =[]
    while i <len(jobs):
        for j in jobs:
            if start < j[0]<=now:
                heapq.heappush(heap,[j[1],[0]])
        if len(heap)>0:
            current = heapq.heappop(heap)
            start = now
            now +=current[0]
            answer+=(now-current[1])
            i+=1
        else:
            now+=1
    return answer//len(jobs)

def practice(jobs:List[int])->int:
    answer, now, i = 0,0,0
    start = -1
    heap =[]
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <=now:
                heapq.heappush(heap,[j[1],j[0]])
        if heap:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer+=(now-current[1])
            i+=1
        else:
            now+=1
    return answer//len(jobs)




TC = int(input())
for test_case in range(1,TC+1):
    jobs = []
    for i in range(int(input())):
        jobs.append(list(map(int,input().split())))
    answer = my(jobs)
    print(answer)