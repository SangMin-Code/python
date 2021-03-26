#2_by_N_tiling.py
import sys
sys.stdin=open('input/2_by_N_tiling')
from typing import List

def my(n:int)->int:
    l = [0]*(n+1)
    l[1],l[2]=1,2
    for i in range(3,n+1):
        if i%2==0:
            l[i] = 2*l[i-2]+l[i-3]
        else :
            l[i]=l[i-1]+l[i-2]
    print(l)
    return l[n]

def test(n:int)->int:
    p,pp,ppp,val = 2,1,0,0
    for i in range(3,n+1):
        if i %2==0:
            val = 2*pp+ppp
        else :
            val = p+pp
        p,pp,ppp= val,p,pp
    return val%1000000007


TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    answer =test(n)
    print(answer)