# 3079.py
import sys
from typing import List

sys.stdin = open('input/3079')


def my(N:int, M:int, checkpoints:List[int])->int:
    left,right = 0, max(checkpoints)*M
    answer =0
    while left<=right:
        temp = 0
        mid = left+(right-left)//2
        for i in checkpoints:
            temp+=(mid//i)
        if temp >= M:
            right = mid-1
            answer = mid
        else :
            left = mid+1
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    N,M = map(int,sys.stdin.readline().rstrip().split())
    checkpoints =[ int(sys.stdin.readline().rstrip()) for _ in range(N)]
    answer = my(N,M,checkpoints)
    print(answer)
