# 1927.py
import sys
from typing import List

sys.stdin = open('input/1927')
import heapq

def my(n:int, nums:List[int]):
    heap = []
    for i in nums:
        if i==0:
            if len(heap)>0:
                print(heapq.heappop(heap))
            else :
                print(0)
        else :
            heapq.heappush(heap,i)

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer=my(n,nums)
