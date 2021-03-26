#expression_with_N.py
#https://programmers.co.kr/learn/courses/30/lessons/42895
import sys
sys.stdin=open('input/expression_with_N')
from typing import List

def my(N:int, number:int)->int:

    s = [set() for _ in range(8) ]
    for i, x in enumerate(s):
        x.add(int(str(N)*(i+1)))
    s[1].add(int(N*N))
    s[1].add(int(N-N))
    s[1].add(int(N+N))
    s[1].add(int(N/N))

    for i in range(2,8):
        for j in range(i):
            for k in s[j]:
                for l in s[i-j-1]:
                    s[i].add(int(k+l))
                    s[i].add(int(k-l))
                    s[i].add(int(k*l))
                    if l!=0:
                        s[i].add(int(k//l))

    for i,val in enumerate(s):
        if number in val:
            return i+1
    return -1

TC = int(input())
for test_case in range(1,TC+1):
    N,number = map(int,input().split())
    answer = my(N,number)
    print(answer)