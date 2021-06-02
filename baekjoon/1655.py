# 1655.py
import sys
from typing import List

sys.stdin = open('input/1655')
import heapq

def my(n:int, nums:List[int]):
    max_h,min_h = [],[]
    for i in nums:
        if len(max_h)==len(min_h):
            heapq.heappush(max_h,[-i,i])
        else:
            heapq.heappush(min_h,[i,i])
        if max_h and min_h and max_h[0][1] > min_h[0][1]:
            max_val = heapq.heappop(max_h)[1]
            min_val = heapq.heappop(min_h)[1]
            heapq.heappush(max_h,[-min_val,min_val])
            heapq.heappush(min_h,[max_val,max_val])
        print(max_h[0][1])
TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    nums = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    answer=my(n,nums)
