# 1654.py
import sys
from typing import List

sys.stdin = open('input/1654')


def my(k:int,n:int,lines:List[int])->int:

    left,right,result,max_val = 0,max(lines),0,0

    while left<=right:
        mid = left+(right-left)//2
        result = sum([i//mid for i in lines])
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
    lines =[]
    for _ in range(k):
        lines.append(int(input()))
    answer = my(k,n,lines)
    print(answer)
