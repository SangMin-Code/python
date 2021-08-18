# Q4.py.py
import sys
from typing import List

sys.stdin = open('input/Q4')


def my(money:List[int])->int:
    dp1 = [0]*len(money)
    dp1[0]=money[0]
    dp1[1]=max(money[0],money[1])
    for i in range(2,len(money)-1):
        dp1[i]=max(dp1[i-1],money[i]+dp1[i-2])

    dp2 = [0]*len(money)
    dp2[0]=0
    dp2[1]=money[1]
    for i in range(2,len(money)):
        dp2[i]=max(dp2[i-1],money[i]+dp2[i-2])
    return max(max(dp1),max(dp2))

def my2(money:List[int])->int:
    dp1 = [0]*len(money)
    dp1[0]=money[0]
    dp1[1]=max(money[0],money[1])
    for i in range(2,len(money)-1):
        dp1[i]=max(dp1[i-1],money[i]+dp1[i-2])

    dp2 = [0]*len(money)
    dp2[0]=0
    dp2[1]=money[1]
    for i in range(2,len(money)):
        dp2[i]=max(dp2[i-1],money[i]+dp2[i-2])
    return max(max(dp1),max(dp2))


TC = int(input())
for test_case in range(1, TC + 1):
    money = list(map(int,input().split()))
    answer = my(money)
    print(answer)
