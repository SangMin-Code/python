# 11577.py
import sys
from typing import List

sys.stdin = open('input/11577')


#시간초과
def my(N:int,S:int, bulbs:List[int]):
    dic = {1:0, 0:1}
    cnt =0
    convert = [0]*N
    for i in range(N-S+1):
        if (bulbs[i]==1 and convert[i]%2==0) or (bulbs[i]==0 and convert[i]%2!=0):
            cnt+=1
            bulbs[i]=0
            for j in range(S):
                convert[i+j]+=1

    for i in range(N):
        if convert[i]%2!=0:
            bulbs[i]=dic[bulbs[i]]

    if sum(bulbs)==0:
        return cnt


    return 'Insomnia'



TC = int(input())
for test_case in range(1, TC + 1):
    N,S = map(int,sys.stdin.readline().rstrip().split())
    bulbs = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(N,S,bulbs)
    print(answer)
