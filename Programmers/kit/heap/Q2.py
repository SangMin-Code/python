# Q1.py
import heapq
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(jobs:List[List[int]])->int:
    answer , time,l = 0,0,len(jobs)
    heapq.heapify(jobs)
    while jobs:
        heap =[]
        while jobs and  jobs[0][0]<=time:
            job = heapq.heappop(jobs)
            heapq.heappush(heap,[job[1],job[0]])
        if heap:
            e = heapq.heappop(heap)
            answer += e[0] + time - e[1]
            time += e[0]
            while heap:
                j = heapq.heappop(heap)
                heapq.heappush(jobs,[j[1],j[0]])
        else:
            time+=1
    return answer//l

def my2(jobs:List[List[int]])->int:
    answer, now, i =0,0,0
    start = -1
    heap = []
    while i < len(jobs):
        for j in jobs:
            if start<j[0]<=now:
                heapq.heappush(heap,[j[1],j[0]])
        if heap:
            current = heapq.heappop(heap)
            start =now
            now += current[0]
            answer += (now-current[1])
            i+=1
        else:
            now+=1
    return answer//len(jobs)

TC = int(input())
for test_case in range(1, TC + 1):
    jobs = [list(map(int,i.split())) for i in input().split(',')]
    answer = my2(jobs)
    print(answer)
