# 2003.py
import sys
from typing import List

sys.stdin = open('input/2003')


def my(n:int,m:int,nums:List[int])->int:
    cnt= 0
    l,r = 0,1
    answer = []
    while l<n:
        while r<n+1:
            val = sum(nums[l:r])
            if val==m:
                cnt+=1
                break
            elif val<m:
                r+=1
            else:
                break
        l+=1
    return cnt


TC = int(input())
for test_case in range(1, TC + 1):
    n,m = map(int,input().split())
    nums = list(map(int,input().split()))
    answer = my(n,m,nums)
    print(answer)
