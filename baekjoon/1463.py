# 1463.py
import sys
from typing import List

sys.stdin = open('input/1463')


def my(n:int)->int:
    nums = [0]*(n+1)
    if n==1:
        return 0
    for i in range(1,n+1):
        if i%6==0:
            nums[i]= min(nums[i//3],nums[i//2],nums[i-1])+1
        elif i%3==0:
            if i//3==1:
                nums[i]=1
            else:
                nums[i]=min(nums[i//3],nums[i-1])+1
        elif i%2==0:
            if i//2==1:
                nums[i]=1
            else:
                nums[i]=min(nums[i//2],nums[i-1])+1
        else:
            nums[i]=nums[i-1]+1
    return nums[n]

TC = int(input())
for test_case in range(1, TC + 1):
    n=int(input())
    answer = my(n)
    print(answer)
