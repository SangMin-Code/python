# Q2.py
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(triangle:List[List[int]])->int:
    answer = 0

    for i,v in enumerate(triangle):
        if i==0:
            continue
        for j,val in enumerate(v):
            if j==0:
                triangle[i][j]+=triangle[i-1][j]
            elif j==len(v)-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
    return max(triangle[-1])

TC = int(input())
for test_case in range(1, TC + 1):
    triangle = [list(map(int,i.split())) for i in input().split(',')]
    answer = my(triangle)
    print(answer)
