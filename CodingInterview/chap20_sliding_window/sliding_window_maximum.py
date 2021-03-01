#sliding_window_maximum.py
import collections


import sys
sys.stdin = open('input/sliding_window_maximum')
from typing import List

def my(k:int, nums:List[int])->List[int]:
    answer = []
    for i in range(len(nums)-k+1):
        answer.append(max(nums[i:i+k]))
    return answer

def max_sliding_window(k:int, nums:List[int])->List[int]:
    results = []
    window = collections.deque()
    current_max= float('-inf')
    for i, v in enumerate(nums):
        window.append(v)
        if i<k-1:
            continue
        if current_max ==float('-inf'):
            current_max = max(window)
        elif v>current_max:
            current_max = v
        results.append(current_max)
        if current_max == window.popleft():
            current_max = float('-inf')
    return results

k = int(input())
nums = list(map(int,input().split()))
#answer = my(k,nums)
answer = max_sliding_window(k,nums)
print(answer)
