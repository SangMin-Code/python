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





TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    answer = my(n)
    print(answer)