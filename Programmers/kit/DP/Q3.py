# Q3.py
import smtplib
import sys
from typing import List

sys.stdin = open('input/Q3')


def my(m:int,n:int,puddles:List[List[int]])->int:
    dir = [[1, 0], [0, 1]]

    def dfs(r, c):
        cnt = 0
        if c == m - 1 and r == n - 1:
            return 1
        for dr, dc in dir:
            nr, nc = dr + r, dc + c
            if 0 <= nr < n and 0 <= nc < m and [nc + 1, nr + 1] not in puddles:
                cnt += dfs(nr, nc)
        return cnt

    return dfs(0, 0)


TC = int(input())
for test_case in range(1, TC + 1):
    m,n = map(int,input().split())
    puddles = [list(map(int,i.split())) for i in input().split(',')]
    answer = my(m,n,puddles)
    print(answer)
