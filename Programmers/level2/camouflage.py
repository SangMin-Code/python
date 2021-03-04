#https://programmers.co.kr/learn/courses/30/lessons/42578

import sys
sys.stdin = open('input/camouflage')
from typing import List
import collections

def my(clothes:List[List[str]])->int:
    answer =1
    count = collections.defaultdict(int)
    for _,part in clothes:
        count[part]+=1
    for i in count:
        answer*=(count[i]+1)
    return answer-1

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    clothes = []
    for _ in range(n):
        clothes.append(list(input().split()))
    answer = my(clothes)
    print(answer)