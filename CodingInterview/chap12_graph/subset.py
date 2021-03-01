import sys
sys.stdin=open('input/subset')
from typing import List


def my(nums:List[int])->List[List[int]]:
    result =[]
    result.append([])
    prev_nums=[]
    def find(idx:int):
        if idx==len(nums):
            return
        for i in range(idx,len(nums)):
            prev_nums.append(nums[i])
            result.append(prev_nums[:])
            find(i+1)
            prev_nums.pop()
    find(0)
    return result

def subset(nums:List[int])->List[List[int]]:
    result = []
    def dfs(index,path):
        result.append(path)
        for i in range(index,len(nums)):
            dfs(i+1,path+[nums[i]])
    dfs(0,[])
    return result


nums = list(map(int,input().split()))
print(my(nums))
print(subset(nums))