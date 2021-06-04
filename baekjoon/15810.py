# 15810.py
import sys
from typing import List

sys.stdin = open('input/15810')


def my(N:int, M:int, staffs:List[int])->int:

    left, right = 0, max(staffs)*M
    answer = 0

    while left<=right:
        mid = left + (right-left)//2
        cnt = 0
        for i in staffs:
            cnt += mid//i
        if cnt >= M:
            right = mid-1
            answer = mid
        else :
            left = mid +1
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    N,M = map(int, sys.stdin.readline().rstrip().split())
    staffs = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(N,M,staffs)
    print(answer)
