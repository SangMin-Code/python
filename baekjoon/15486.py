# 15486.py
import sys
from typing import List

sys.stdin = open('input/15486')


def my(n:int, schedule:List[List[int]])->int:
    dp =[0]*(n+1)
    t,p,m = [],[],0
    for i,j in schedule:
        t.append(i)
        p.append(j)
    for i in range(n):
        m=max(m,dp[i])
        if i+t[i]>n:
            continue
        dp[i+t[i]]=max(m+p[i],dp[i+t[i]])
    return max(dp)

def my2(n:int, schedule:List[List[int]])->int:
    t,p,dp,m=[],[],[0]*(n+1),0

    for i,j in schedule:
        t.append(i)
        p.append(j)
    for i in range(n):
        m=max(m,dp[i])
        if i+t[i]>n:
            continue
        dp[i+t[i]] = max(m+p[i],dp[i+t[i]])
    return max(dp)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    schedule = [list(map(int,input().split())) for _ in range(n)]
    answer = my(n,schedule)
    print(answer)
