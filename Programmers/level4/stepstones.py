# stepstones.py
import sys
from typing import List

sys.stdin = open('input/stepstones')


def my(d:int, n:int, rocks:List[int])->int:
    rocks.sort()
    left,right = 0, d
    rocks.append(d)
    answer=0
    while left<=right:
        mid = left + (right-left)//2
        max_min = d
        current, cnt = 0,0

        for rock in rocks:
            diff = rock-current
            if diff < mid :
                cnt+=1
            else :
                current = rock
                max_min = min(max_min,diff)

        if cnt >n:
            right = mid-1
        else :
            left = mid+1
            answer = max_min
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    d,n = map(int,input().split())
    rocks = list(map(int,input().split()))
    answer = my(d,n,rocks)
    print(answer)
