'''
https://programmers.co.kr/learn/courses/30/lessons/42626
heap/더 맵게게'''

import sys
sys.stdin = open('input/hotter')
import heapq
from typing import List


def my(k:int, foods:List[int])->int:
    heap = []
    for i in foods:
        heapq.heappush(heap,i)
    result = 0
    while heap[0]<k:
        food1 = heapq.heappop(heap)
        food2 = heapq.heappop(heap)
        heapq.heappush(heap,food1+food2*2)
        result+=1
    if heap[0]<k and len(heap)<2:
        return -1
    return result

k = int(input())
foods = list(map(int,input().split()))
print(my(k,foods))

