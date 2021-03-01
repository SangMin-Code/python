import sys
sys.stdin = open('input/binary_search')
from typing import List
import bisect
def my(nums:List[int],k:int):
    def find(left, right,target:int):
        if left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                return find(left, mid-1,target)
            elif nums[mid]<target:
                return find(mid+1,right,target)
        else:
            return -1
    return find(0,len(nums)-1,k)

def recursion(nums:List[int], target:int)->int:
    def binary_search(left,right):
        if left<=right:
            mid = (left+right)//2
            #TODO 자료형을 넘지 않는 방식의 계산
            #mid = left + (right-left)//2
            if nums[mid] < target:
                return binary_search(mid+1,right)
            elif nums[mid]> target:
                return binary_search(left,mid-1)
            else :
                return mid
        else :
            return -1
    return binary_search(0,len(nums)-1)

def iterator(nums:List[int],target:int)->int:
    left, right = 0, len(nums)-1
    while left<=right:
        mid = (left+right)//2
        if  nums[mid]<target:
            left = mid+1
        elif nums[mid]>target:
            right = mid-1
        else :
            return mid
    return -1

def using_module(nums:List[int], target:int)->int:
    index = bisect.bisect_left(nums,target)
    if index<len(nums) and nums[index]==target:
        return index
    else :
        return -1

def using_index(nums:List[int], target:int)->int:
    try:
        return nums.index(target)
    except ValueError:
        return -1



target = int(input())
nums = list(map(int,input().split()))
answer =my(nums,target)
print(answer)