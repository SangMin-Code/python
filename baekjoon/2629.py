# 2629.py
import copy
import sys
from typing import List

sys.stdin = open('input/2629')

def my(n:int,m:int,weights:List[int],beads:List[int])->List[str]:
    candidates = set([weights[0]])
    for weight in weights[1:]:
        next_candidates = set()
        for pre in candidates:
            next_candidates.add(pre)
            next_candidates.add(pre+weight)
            if(weight>pre):
                next_candidates.add(weight-pre)
        candidates = copy.deepcopy(next_candidates)
    print(candidates)
    answer = []
    for bead in beads:
        if bead in candidates:
            answer.append('Y')
        else:
            answer.append('N')
    return answer

def my2(n:int,m:int,weights:List[int],beads:List[int])->List[str]:
    dp = [[0]*40001 for _ in range(n+1)]
    dp[0][0]=1
    for i in range(1,n+1):
        now = weights[i-1]
        for j in range(40001):
            if dp[i-1][j]:
                dp[i][j] = 1
                tmp = [j-now, j+now, now-j, now+j]
                for t in tmp:
                    if 0<=t<=40000:
                        dp[i][t]=1
    answer = ['N']*m
    for i in range(m):
        if dp[n][beads[i]]:
            answer[i]='Y'
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(input())
    weights = list(map(int,input().split()))
    m=int(input())
    beads = list(map(int,input().split()))
    answer = my2(n,m,weights,beads)
    print(' '.join(answer))
