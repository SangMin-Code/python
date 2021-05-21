# 4779.py
import sys
from typing import List

sys.stdin = open('input/4779')


def my(n:int)->str:

    def dfs(s,k):
        if k==0:
            return '-'
        elif k>0:
            new_s = len(s)//3 * '_'
            return dfs(new_s,k-1)+len(new_s)*' '+dfs(new_s,k-1)
    return dfs('-'*3**n,n)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    answer = my(n)
    print(answer)
