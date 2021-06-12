# 11722.py
import sys
from typing import List

sys.stdin = open('input/11722')


def my(n:int,nums:List[int])->int:
    dp = [1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if nums[i] < nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(input())
    nums = list(map(int,input().split()))
    answer = my(n,nums)
    print(answer)
