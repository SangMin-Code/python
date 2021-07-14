# Q3.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q3')

def my(clothes:List[List[str]])->int:
    dic = collections.defaultdict(int)
    for i,j in clothes:
        dic[j]+=1
    answer = 1
    for key in dic.keys():
        answer*=(dic[key]+1)
    return answer-1

TC = int(input())
for test_case in range(1, TC + 1):
    clothes =[list(i.split()) for i in list(input().split(','))]
    answer = my(clothes)
    print(answer)

