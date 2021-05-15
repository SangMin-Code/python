# 1769.py
import sys
from typing import List

sys.stdin = open('input/1769')


def my(n:str):

    if len(n)==1 and int(n)%3==0:
        return [0,"YES"]

    cnt = 0
    while len(n)>1:
        t = 0
        for i in n:
            t+=int(i)
        n = str(t)
        cnt+=1

    if int(n)%3==0:
        return [cnt,"YES"]
    else :
        return [cnt,"NO"]

TC = int(input())
for test_case in range(1, TC + 1):
    n = sys.stdin.readline().rstrip()
    answer = my(n)
    for i in answer:
        print(i)
