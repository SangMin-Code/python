# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(N:int,number:List[int])->int:
    vals = [{str(N) * i} for i in range(10)]

    for i in range(2,10):
        for j in range(1,i):
            for k in vals[j]:
                for l in vals[i-j]:
                    v1,v2 = int(k),int(l)
                    vals[i].add(str(v1+v2))
                    vals[i].add(str(v1-v2))
                    vals[i].add(str(v1*v2))
                    if v2:
                        vals[i].add(str(v1//v2))

    for i,val in enumerate(vals):
        if str(number) in val:
            return i
    return -1

TC = int(input())
for test_case in range(1, TC + 1):
    N,number = map(int,input().split())
    answer = my(N,number)
    print(answer)
