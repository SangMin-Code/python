# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q3')


def my(brown:int,yellow:int)->List[int]:
    for i in range(1,yellow+1):
        width = i
        if yellow%i!=0:
            continue
        height = yellow//width
        if brown == 2*(width+2)+(2*height):
            return [height+2,width+2]
    return [-1,-1]

TC = int(input())
for test_case in range(1, TC + 1):
    brown,yellow = map(int,input().split())
    answer = my(brown,yellow)
    print(answer)
