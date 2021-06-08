# 11049.py
import sys
from typing import List

sys.stdin = open('input/11049')


def my(n:int, matrix:List[List[int]])->int:
    dp = [[0]*(n+1) for _ in range(n+1)]
    d= []
    for i,j in matrix:
        d.append(i)
    d.append(matrix[-1][-1])

    for l in range(1,n):
        for i in range(1,n-l+1):
            j=i+l
            dp[i][j]=min([dp[i][k]+dp[k+1][j]+d[i-1]*d[k]*d[j] for k in range(i,j)])
    return dp[1][n]

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    answer = my(n,matrix)
    print(answer)
