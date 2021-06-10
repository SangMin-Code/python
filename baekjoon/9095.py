# 9095.py
import sys
from typing import List

sys.stdin = open('input/9095')


def my(n:int):
    #1<=n<=11
    dp = [0]*12
    dp[1],dp[2],dp[3]=1,2,4
    if n<=3:
        return dp[n]
    for i in range(4,n+1):
        dp[i]= dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]


TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    answer = my(n)
    print(answer)
