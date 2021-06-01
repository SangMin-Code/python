# 12015.py
import sys
from typing import List
import bisect
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

def my2(n:int,nums:List[int])->int:
    dp = []

    for i in nums:
        k = bisect.bisect_left(dp, i)  # 자신이 들어갈 위치 k
        if len(dp) <= k:  # i가 가장 큰 숫자라면
            dp.append(i)
        else:
            dp[k] = i  # 자신보다 큰 수 중 최솟값과 대체
    return len(dp)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    nums = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my2(n,nums)
    print(answer)
