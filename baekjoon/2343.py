# 2343.py
import sys
from typing import List

sys.stdin = open('input/2343')


def my(N:int, M:int,lessons:List[int])->int:

    left = max(lessons)
    right = sum(lessons)
    answer = 0

    while left<=right:
        mid = left+(right-left)//2
        cnt = 1
        temp_sum = 0
        for i in lessons:
            if temp_sum+i>mid:
                cnt+=1
                temp_sum=0
            temp_sum+=i
        if cnt<=M:
            right = mid-1
            answer = mid
        else :
            left = mid+1
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    N,M = map(int,sys.stdin.readline().rstrip().split())
    lessons = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(N,M,lessons)
    print(answer)
