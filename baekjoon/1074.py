# 1074.py
import sys
from typing import List

sys.stdin = open('input/1074')


def my(N:int,r:int,c:int)->int:
    def dfs(n,r,c):
        cnt,l = 0, 2**(n-1)
        if n>0:
            if r<l and c<l:
                cnt += dfs(n-1,r,c)
            elif r<l and c>=l:
                cnt=l**2 + dfs(n-1,r,c-l)
            elif r>=l and c<l:
                cnt+=l**2*2+dfs(n-1,r-l,c)
            elif r>=l and c>=l:
                cnt+=l**2*3+dfs(n-1,r-l,c-l)
        return cnt
    return dfs(N,r,c)

TC = int(input())
for test_case in range(1, TC + 1):
    N,r,c = map(int,sys.stdin.readline().rstrip().split())
    answer = my(N,r,c)
    print(answer)
