# 12015.py
import sys
from typing import List

sys.stdin = open('input/12015')


def my(n:int, nums:List[int])->int:
    nums.sort()
    num = nums[0]

    def search(num,start):
        left = start
        right = len(nums)-1
        result = 0
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid] <=num:
                result = left
                left =mid+1
            else :
                if nums[mid]>num:
                    result = mid
                right = mid-1
        return result

    cnt = 0
    idx = 0
    while idx<len(nums)-1:
        idx = search(num,idx)
        num = nums[idx]
        cnt += 1
    return cnt

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(n,nums)
    print(answer)
