import sys
sys.stdin = open('input/kth_largest_element_in_an_array')
from typing import List
import heapq

def my(k:int, nums:List[int])->int:
    array = sorted(nums,reverse=True)
    return array[k-1]

def using_heapq(nums:List[int],k:int)->int:
    heap = list()
    for n in nums:
        heapq.heappush(heap,-n)
    for _ in range(k):
        heapq.heappop(heap)
    return -heapq.heappop(heap)

def using_heapify(nums:List[int],k:int)->int:
    heapq.heapify(nums)
    for _ in range (len(nums)-k):
        heapq.heappop(nums)
    return heapq.heappop(nums)

def using_nlargest(nums:List[int],k:int)->int:
    return heapq.nlargest(k,nums)[-1]

def using_sort(nums:List[int],k:int)->int:
    nums.sort()
    return nums[-k]
    #return sorted(nums,reverse=True)[k-1]


k = int(input())
nums = list(map(int,input().split()))
answer = my(k,nums)
print(answer)