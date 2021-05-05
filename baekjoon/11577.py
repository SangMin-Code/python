# 11577.py
import sys
from typing import List

sys.stdin = open('input/11577')


#시간초과
def my(N:int,S:int, bulbs:List[int]):
    dic = {1:0, 0:1}
    light = sum(bulbs)
    cnt =0
    for i in range(N-S+1):
        if bulbs[i]==1:
            cnt+=1
            for j in range(S):
                bulbs[i+j] = dic[bulbs[i+j]]
                if bulbs[i+j]==1:
                    light+=1
                else :
                    light-=1
        if light==0:
            return cnt
    return 'Insomnia'



TC = int(input())
for test_case in range(1, TC + 1):
    N,S = map(int,sys.stdin.readline().rstrip().split())
    bulbs = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(N,S,bulbs)
    print(answer)
