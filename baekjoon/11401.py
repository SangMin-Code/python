# 11401.py
import math
import sys
from typing import List

sys.stdin = open('input/11401')


def my(n:int,k:int)->int:
    mod = 1000000007
    a,b=1,1

    #n!
    for i in range(1,n+1):
        a*=i
        a%=mod
    #k!
    for i in range(1,k+1):
        b*=i
        b%=mod
    #(n-k)!
    for i in range(1,n-k+1):
        b*=i
        b%=mod
    #b**(mod-2)

    ex = mod-2
    result = 1
    while ex:
        if ex%2:
            result*=b
            result%=mod
        b*=b
        b%=mod
        ex//=2

    return (a*result)%mod

def my2(n:int,k:int)->int:
    a,b,mod,ex=1,1,1000000007,1000000007-2

    for i in range(1,n+1):
        a*=i
        a%=mod
    for i in range(1,k+1):
        b*=i
        b%=mod
    for i in range(1,n-k+1):
        b*=i
        b%=mod

    # n제곱 구하기 ( 2**10 -> (2*2**2)**2 방식으로 구하기)
    ex_result = 1
    while ex:
        if ex%2:
            ex_result*=b
            ex_result%=mod
        b*=b
        b%=mod
        ex//=2
    return (a*ex_result)%mod


TC = int(input())
for test_case in range(1, TC + 1):
    n,k = map(int,sys.stdin.readline().rstrip().split())
    answer = my2(n,k)
    print(answer)
