# 11729.py
import sys
from typing import List

sys.stdin = open('input/11729')


def my(n:int)->List[List[str]]:

    answer = []
    def DFS(floor, start, middle, end):
        if floor == 1:
            answer.append([start,end])
        else :
            DFS(floor-1,start,end,middle)
            answer.append([start,end])
            DFS(floor-1,middle,start,end)
    cnt = 1
    for i in range(n-1):
        cnt =cnt*2+1
    answer.append([cnt])
    DFS(n,1,2,3)
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    n=int(sys.stdin.readline().rstrip())
    answer = my(n)
    for i in answer:
        print(' '.join([str(j) for j in i]))

