# 2470.py
import sys
from typing import List

sys.stdin = open('input/2470')


def my(n:int,solutions:List[int])->List[str]:
    solutions.sort()
    pl,pr = 0, n-1
    limit = solutions[pl]+solutions[pr]
    idx1,idx2 = 0,0

    while pl<pr:
        mix = solutions[pl]+solutions[pr]
        if abs(mix)<=abs(limit):
            limit = mix
            idx1 = pl
            idx2 = pr
            if limit ==0:
                break
        if  mix>0:
            pr-=1
        else:
            pl+=1
    return list(map(str,[solutions[idx1],solutions[idx2]]))

TC = int(input())
for test_case in range(1, TC + 1):
    n= int(sys.stdin.readline().rstrip())
    solutions= list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(n,solutions)
    print(' '.join(answer))
