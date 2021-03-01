#TwoSum.py

import sys
from builtins import enumerate
from typing import List
sys.stdin = open('input/TwoSum')

def my(nums:List[int], target:int)->List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n,1):
            if nums[i]+nums[j]==target:
                return [i,j]
def brute_force(nums:List[int], target:int)->List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1,n,1):
            if nums[i]+nums[j]==target:
                return [i,j]
def using_in(nums:List[int],target:int)->List[int]:
    for i, n in enumerate(nums):
        complement = target-n
        if complement in nums[i+1:]:
            return nums.index(n),nums[i+1:].index(complement)+i+1

def using_dic1(nums:List[int],target:int)->List[int]:
    nums_map={}
    #키와 값을 바꿔서 딕셔너리로 저장
    for i,num in enumerate(nums):
        nums_map[num]=i
    #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i,num in enumerate(nums):
        if target - num in nums_map and i !=nums_map[target-num]:
            return nums.index(num), nums_map[target-num]

def using_dic2(nums:List[int],target:int)->List[int]:
    nums_map={}
    #하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target -num in nums_map:
            return [nums_map[target-num],i]
        nums_map[num]=i

def two_point(nums:List[int],target:int)->List[int]:
    left, right = 0, len(nums)-1
    while not left ==right:
        #합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left]+nums[right]<target:
            left+=1
        #합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left]+nums[right]>target:
            right-=1
        else:
            return left,right
        #항상 nums 가 정렬이 되어있다는 정보를 알 수 없으므로 문제가 발생

nums = list(map(int,input().split()))
target = int(input())

print(using_in(nums,target))