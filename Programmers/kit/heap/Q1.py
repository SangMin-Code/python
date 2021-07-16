# Q1.py
import heapq
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(scoville:List[int],K:int)->int:
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K and len(scoville)>1:
        f1 = heapq.heappop(scoville)
        f2 = heapq.heappop(scoville)
        heapq.heappush(scoville,f1+f2*2)
        answer+=1
    if scoville[0]<K:
        return -1
    return answer

def my2(scoville:List[int],K:int)->int:

    scoville.sort()
    def bserch(n,list):
        start,end,mid = 0,len(list)-1,0
        while start<=end:
            mid = (start+end)//2
            if list[mid]>=n:
                end = mid-1
            else :
                start = mid+1
        return mid

    def push(n,list):
        next_list = list[:]
        idx = bserch(n,next_list)
        if idx == len(list)-1:
            return next_list[:]+[n]
        else:
            return next_list[:idx]+[n]+next_list[idx:]

    answer = 0

    while scoville[0]<K and len(scoville)>1:
        f1=scoville.pop(0)
        f2=scoville.pop(0)
        scoville = push(f1+f2*2,scoville)
        answer+=1
    if scoville[0]<K:
        return -1
    return answer




TC = int(input())
for test_case in range(1, TC + 1):
    scoville = list(map(int,input().split()))
    K = int(input())
    answer = my2(scoville,K)
    print(answer)
