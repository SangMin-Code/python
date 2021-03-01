#ArrayPartition
import sys
from typing import List
sys.stdin = open('input/ArrayPartiotion')

def my(nums:List[int])->int:
    sum=0
    nums.sort(reverse=True)
    for i in range(len(nums)):
        if i%2!=0:
            sum+=nums[i]
    return sum

def pair(nums:List[int])->int:
    sum=0
    pair=[]
    nums.sort()

    for n in nums:
        #앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair)==2:
            sum+=min(pair)
            pair=[]
    return sum

def even(nums:List[int])->int:
    sum =0
    nums.sort()
    for i, n in enumerate(nums):
        if i%2==0:
            sum+=n
    return sum

def slicing(nums:List[int])->int:
    return sum(sorted(nums)[::2])





nums = list(map(int,input().split()))
print(my(nums))