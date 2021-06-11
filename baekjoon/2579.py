# 2579.py
import sys
from typing import List

sys.stdin = open('input/2579')


def my(n:int,stairs:List[int])->int:

    dp=[0]*(n+1)
    dp[1]=sum(stairs[:1])
    dp[2]=sum(stairs[:2])
    dp[3]=sum(stairs[:3])

    for i in range(3,n+1):
        dp[i]= max(dp[i-3]+stairs[i-2]+stairs[i-1],dp[i-2]+stairs[i-1])
    print(dp)
    return dp[n]

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(input())
    stairs = [int(input()) for _ in range(n)]
    answer = my(n,stairs)
    print(answer)
