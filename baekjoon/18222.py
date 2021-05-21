# 18222.py
import collections
import sys
from typing import List

sys.stdin = open('input/18222')


def my(n:int)->str:
    k,l = 0,1
    reverse = False
    lengths = collections.defaultdict(int)
    while l<n:
        lengths[k]=l
        k+=1
        l=2**k

    def dfs(idx,e,r):
        if idx ==1 :
            if r :
                return "1"
            else :
                return "0"
        if idx>lengths[e-1]:
            r = not r
            return dfs(idx-lengths[e-1],e-1,r)
        else :
            return dfs(idx,e-1,r)
    return dfs(n,k,False)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    answer = my(n)
    print(answer)
