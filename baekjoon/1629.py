# 1629.py
import sys
from typing import List

sys.stdin = open('input/1629')


def my(a:int,b:int,c:int)->int:
    def divide(num,ex):
        n =0
        if ex==0:
            return 1
        elif ex%2==0:
            n=divide(num,ex//2)
            return n**2%c
        else:
            n=divide(num,(ex-1)//2)
            return num*n**2%c
    return divide(a,b)%c

TC = int(input())
for test_case in range(1, TC + 1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    answer = my(a,b,c)
    print(answer)
