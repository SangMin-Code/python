#best-time-to-buy-and=self-stock

import sys
from typing import List
sys.stdin = open('input/best-time-to-buy-and=self-stock')

def my(nums:List[int])->int:
    n = len(nums)
    maxVal =0
    for i in range(n-1):
        val = max(nums[i:])-nums[i]
        if val>maxVal : maxVal = val
    return maxVal

def bruteForce(nums:List[int])->int:
    max_price =0
    for i,price in enumerate(nums):
        for j in range(i,len(nums)):
            max_price = max(nums[j]-price,max_price)
    return max_price

def min_max(nums:List[int])->int:
    profit = 0
    min_price=sys.maxsize

    #최댓값과 최솟값을 계속 갱신
    for price in nums:
        min_price= min(price,min_price)
        profit = max(profit,price-min_price)
    return profit

nums = list(map(int,input().split()))
print(my(nums))
