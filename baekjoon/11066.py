# 11066.py
import collections
import sys
from typing import List

sys.stdin = open('input/11066')


def my(k:int, files:List[int])->int:
    #s[i] 는 1번부터 i번까지의 누적합
    s = [0 for _ in range(k+1)]
    for i in range(1,k+1):
        s[i]=s[i-1]+files[i]
    #dp[i][j] : i에서 j까지 합하는데 필요한 최소 비용
    #dp[i][l]+dp[l+1][j] + sum(files[i]~files[j])
    dp = [[0]*(k+1) for _ in range(k+1)]
    for i in range(2,k+1):
        for j in range(1,k+2-i):
            dp[j][j+i-1]=min([dp[j][j+l]+dp[j+l+1][j+i-1] for l in range(i-1)])+s[j+i-1]-s[j-1]
    return dp[1][k]



TC = int(input())
for test_case in range(1, TC + 1):
    k = int(sys.stdin.readline().rstrip())
    files = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(k, files)
    print(answer)
