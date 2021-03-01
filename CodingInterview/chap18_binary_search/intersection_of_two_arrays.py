import sys
sys.stdin = open('input/intersection_of_two_arrays')
from typing import List,Set
import bisect


def my(nums1:List[int], nums2:List[int])->List[int]:
    answer = [num for num in nums1 if num in nums2]
    return list(set(answer))


def brute_force(nums1:List[int],nums2:List[int])->List[int]:
    result:Set= set()
    for n1 in nums1:
        for n2 in nums2:
            if n1 ==n2:
                result.add(n1)
    return result

def binary_serach(nums1:List[int],nums2:List[int])->List[int]:
    result:Set =set()
    nums2.sort()
    for n1 in nums1:
        i2 = bisect.bisect_left(nums2,n1)
        if len(nums2)>0 and len(nums2)>i2 and n1==nums2[i2]:
            result.add(n1)
    return result

def two_points(num1:List[int],num2:List[int])->List[int]:
    result:Set = set()
    num1.sort()
    num2.sort()
    i=j=0
    while i<len(num1) and j <len(num2):
        if num1[i]>num2[j]:
            j+=1
        elif num1[i]<num2[j]:
            i+=1
        else :
            result.add(num1[i])
            i+=1
            j+=1
    return result




TC = int(input())
for test_case in range(1,TC+1):
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    answer = my(nums1,nums2)
    print(answer)