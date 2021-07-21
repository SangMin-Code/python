# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(n:int,lost:List[int],reserve:List[int])->int:
    lost.sort()
    reserve.sort()

    temp = reserve[:]
    for i in temp:
        if i in lost:
            lost.remove(i)
            reserve.remove(i)

    n-=len(lost)

    for i in lost:
        if i+1 in reserve:
            reserve.remove(i+1)
            n+=1
        elif i-1 in reserve:
            reserve.remove(i-1)
            n+=1

    return n


TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    lost = list(map(int,input().split()))
    reserve = list(map(int,input().split()))
    answer = my(n,lost,reserve)
    print(answer)
