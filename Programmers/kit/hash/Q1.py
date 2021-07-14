# Q1.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(participant:List[str],completion:List[str])->str:

    dic = collections.defaultdict(int)
    for i in completion:
        dic[i]+=1
    for i in participant:
        dic[i]-=1
        if dic[i]<0:
            return i

TC = int(input())
for test_case in range(1, TC + 1):
    participant = list(input().split())
    completion = list(input().split())
    answer = my(participant,completion)
    print(answer)
