# 2110.py
import sys
from typing import List

sys.stdin = open('input/2110')

def my(k:int,n:int,houses:List[int])->int:
    houses.sort()

    left,right,max_val = 1, houses[-1]-houses[0],0

    while left <= right:

        mid = left+(right-left)//2

        result = 1

        start = houses[0]

        for i in range(1,k):
            if houses[i]-start >=mid:
                result+=1
                start = houses[i]

        if result>=n:
            left = mid+1
            if mid >max_val:
                max_val=mid
        else :
            right = mid-1

    return max_val


TC = int(input())
for test_case in range(1, TC + 1):
    k,n = map(int,input().split())
    houses =[]
    for _ in range(k):
        houses.append(int(input()))
    answer = my(k,n,houses)
    print(answer)
