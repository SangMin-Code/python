#match_expect.py
#https://programmers.co.kr/learn/courses/30/lessons/12985
import sys
sys.stdin=open('input/match_expect')
from typing import List
from math import ceil

def my(N:int, A:int,B:int)->int:
    round = 0
    while A!=B:
        round+=1
        A=(A+1)//2
        B=(B+1)//2
    return round

def practce(N:int, A:int, B:int)->int:
    round = 0
    while A!=B:
        round+=1
        A=(A+1)//2
        B=(B+1)//2
    return round

TC = int(input())
for test_case in range(1,TC+1):
    N,A,B = map(int,input().split())
    answer = my(N,A,B)
    print(answer)