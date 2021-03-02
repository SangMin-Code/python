import sys
sys.stdin = open('input/majority_elements')
from typing import List
import collections


def my(nums:List[int])->int:
    num = collections.Counter(nums)
    for i in num:
        if num[i] > len(nums)//2:
            return i

def brute_force(nums:List[int])->int:
    for num in nums:
        if nums.count(num) > len(nums)//2:
            return num

def dynamic_programming(nums:List[int])->int:
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num]==0:
            counts[num]=nums.count(num)
        if counts[num]>len(nums)//2:
            return num
    #Memoization을 이용한 간단한 다이나믹 프로그래밍 풀이

def divide_and_conquer(nums:List[int])->int:
    if not nums:
        return None
    if len(nums)==1:
        return nums[0]
    half = len(nums)//2
    a=divide_and_conquer(nums[:half])
    b=divide_and_conquer(nums[half:])
    return [b,a][nums.count(a)>half]
    #비둘기집 원리에 따라 과반수를 차지하는 num이 끝까지 살아남아 과반수를 유지할 것

def pythonic(nums:List[int])->int:
    return sorted(nums)[len(nums)//2]
    #정렬하여 가운데를 지정하면 과반수 이상인 num 일 것

TC = int(input())
for text_case in range(1,TC+1):
    nums = list(map(int,input().split()))
    answer = my(nums)
    print(answer)