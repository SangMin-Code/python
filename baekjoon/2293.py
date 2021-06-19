# 2293.py
import collections
import sys
from typing import List

sys.stdin = open('input/2293')


def my(n:int, k:int, coins:List[int])->int:

    dp = [0 for i in range(k + 1)]
    dp[0]=1

    for i in coins:
        for j in range(1, k + 1):
            if j - i >= 0:
                dp[j] += dp[j - i]
    return dp[k]

TC = int(input())
for test_case in range(1, TC + 1):
    n,k = map(int,input().split())
    coins = [int(input())for _ in range(n)]
    answer = my(n,k,coins)
    print(answer)

dp = [ 0 for i in range(k+1)]
dp[0]=1

'asdasd'.lstrip()


