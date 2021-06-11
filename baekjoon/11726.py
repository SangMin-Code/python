# 11726.py
import sys
from typing import List

sys.stdin = open('input/11726')


def my(n:int)->int:

    dp = [0]*(1000+1)
    dp[0],dp[1],dp[2]=0,1,2
    for i in range(3,n+1):
        dp[i]=dp[i-2]+dp[i-1]
    return dp[n]%10007


TC = int(input())
for test_case in range(1, TC + 1):
    n=int(input())
    answer = my(n)
    print(answer)
