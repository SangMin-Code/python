# 2805.py
import sys
from typing import List

sys.stdin = open('input/2805')



def my(k:int,n:int,trees:List[int])->int:

    left,right,result,max_val = 0,max(trees),0,0

    while left<=right:
        mid = left+(right-left)//2
        result = 0
        for i in trees:
            if i-mid>0:
                result+= i-mid

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
    trees = list(map(int,input().split()))
    answer = my(k,n,trees)
    print(answer)

