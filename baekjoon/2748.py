# 2748.py
import sys
from typing import List

sys.stdin = open('input/2748')


def my(n:int)->int:
    a,b=0,1
    for i in range(1,n):
        a,b=b,a+b
    return b


TC = int(input())
for test_case in range(1, TC + 1):
    n= int(input())
    answer = my(n)
    print(answer)
