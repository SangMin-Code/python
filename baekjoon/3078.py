# 3078.py
import sys
from typing import List

sys.stdin = open('input/3078')
import collections

def my(N:int, K:int, friends:List[str]):
    dic = collections.defaultdict(int)
    cnt =0
    start = -K
    end=0
    for i in range(N):
        cnt += dic[len(friends[end])]
        dic[len(friends[end])]+=1
        if start >=0:
            dic[len(friends[start])]-=1
        start +=1
        end +=1
    return cnt

TC = int(input())
for test_case in range(1, TC + 1):
    N,K = map(int,sys.stdin.readline().rstrip().split())
    friends = []
    for _ in range(N):
        friends.append(sys.stdin.readline().rstrip())
    answer = my(N,K,friends)
    print(answer)
