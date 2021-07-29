# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(n:int,times:List[int])->int:
    answer =0
    left= 1
    right = max(times)*n
    while left<=right:
        mid = left+(right-left)//2
        cnt = 0
        for time in times:
            cnt += mid//time
        if cnt>=n:
            answer = mid
            right = mid-1
        else :
            left = mid+1
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    n=int(input())
    times = list(map(int,input().split()))
    answer = my()
    print(answer)
