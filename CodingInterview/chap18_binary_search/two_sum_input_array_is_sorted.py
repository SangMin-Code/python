import sys
sys.stdin = open('input/two_sum_input_array_is_sorted')
from typing import List
import bisect

def my(target:int, numbers:List[int])->List[int]:
    nums = [x for x in numbers if x <=target]
    for idx, num in enumerate(nums):
        another = target - num
        left, right = idx+1, len(nums)-1
        while left<=right:
            mid = left +(right-left)//2
            if nums[mid]>another:
                right = mid-1
            elif nums[mid]<another:
                left= mid+1
            else :
                return [idx+1, mid+1]
    return -1,-1

def using_two_pointers(numbers:List[int], target:int)->List[int]:
    left, right = 0, len(numbers)-1
    while not left == right:
        if numbers[left]+numbers[right]<target:
            left+=1
        elif numbers[left]+numbers[right]>target:
            right-=1
        else:
            return left+1,right+1

def binart_search(nubers:List[int], target:int)->List[int]:
    for k, v in enumerate(nubers):
        left, right = k+1, len(numbers)-1
        expected = target -v
        while left<=right:
            mid = left + (right-left)//2
            if numbers[mid]<expected:
                left=mid+1
            elif nubers[mid]>expected:
                right = mid-1
            else:
                return k+1, mid+1

def using_bisect_module(numbers:List[int], target:int)->List[int]:
    for k,v in enumerate(numbers):
        expected = target-v
        i = bisect.bisect_left(numbers,expected,k+1)
        if i <len(numbers) and numbers[i]==expected:
            return k+1, i+k+2
    #TODO  과도한 슬라이싱은 속도 저하의 주범


target = int(input())
numbers = list(map(int,input().split()))
answer = my(target, numbers)
print(answer)