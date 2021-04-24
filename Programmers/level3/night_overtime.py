#night_overtime
import sys
sys.stdin=open('input/night_overtime')
from typing import List
import heapq

def my(n:int,works:List[int])->int:
    answer = []

    if sum(works) <= n:
        return 0

    works = [-i for i in works]
    heapq.heapify(works)
    while n>0:
        heapq.heappush(works,heapq.heappop(works)+1)
        n-=1
    answer = sum([i**2 for i in works])
    return answer
2
TC = int(input())
for test_case in range(1,TC+1):
    n= int(input())
    works = list(map(int,input().split()))
    answer = my(n,works)
    print(answer)