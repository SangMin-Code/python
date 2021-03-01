import sys
sys.stdin = open('input/search_in_rotated_sorted_array')
from typing import List

def my(nums:List[int],target:int)->int:
    pivot = nums.index(min(nums))
    sorted_nums = nums[pivot:]+nums[:pivot]

    left, right, index = 0, len(nums)-1, -1
    while left<=right:
        mid = left +(right-left)//2
        if sorted_nums[mid]<target:
            left = mid+1
        elif sorted_nums[mid]>target:
            right = mid-1
        else :
            index = mid
            break
    if index == -1:
        return -1
    else :
        return pivot+index


def search(nums:List[int], target:int)->int:
    if not nums:
        return -1

    left, right = 0, len(nums)-1
    while left< right:
        mid = left+(right-left)//2
        if nums[mid]>nums[right]:
            left = mid+1
        else :
            right = mid
    pivot = right

    left, right = 0, len(nums)-1
    while left<=right:
        mid = left+(right-left)//2
        mid_pivot = (mid+pivot)%len(nums)

        if nums[mid_pivot]<target:
            left = mid+1
        elif nums[mid_pivot]>target:
            right = mid=1
        else :
            return mid_pivot
    return -1



target = int(input())
nums = list(map(int,input().split()))

answer = my(nums,target)
print(answer)