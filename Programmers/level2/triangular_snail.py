#triangular_snail.py
import sys
sys.stdin=open('input/triangular_snail')
from typing import List

def my(n:int)->List[int]:
    x,y= n-1,0
    result = [[i+1]*(i+1) for i in range(n)]
    val = n+1
    n-=1
    while True:
        if n==0:
            break
        for i in range(n):
            y += 1
            result[x][y]=val
            val+=1
        n-=1

        if n==0:
            break
        for i in range(n):
            x-=1
            y-=1
            result[x][y] = val
            val+=1
        n-=1

        if n ==0:
            break
        for i in range(n):
            x += 1
            result[x][y]=val
            val+=1
        n-=1
    answer = []
    for i in result:
        answer.extend(i)
    return answer

def practice(n:int)->List[int]:
    snail=[[i]*i for i in range(1,n+1)]
    di = [[0,1],[-1,-1],[1,0]]
    di_idx=0
    val = n+1
    dx,dy = n-1,0
    n-=1
    while True:
        for _ in range(n):
            dx += di[di_idx][0]
            dy += di[di_idx][1]
            snail[dx][dy]=val
            val+=1
        n-=1
        di_idx=(di_idx+1)%3
        if n ==0:
            break
    answer =[]
    for i in snail:
        answer.extend(i)
    return answer

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    #answer = my(n)
    answer = practice(n)
    print(answer)