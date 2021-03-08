#hopscotch.py
import sys
sys.stdin=open('input/hopscotch')
from typing import List

def my(nums:List[List[int]])->int:
    max =[0]
    #n행 4열
    def dfs(n,k,val):
        if k == len(nums):
            if val > max[0]:
                max[0]=val
        elif k<len(nums):
            for i in range(4):
                if i !=n:
                    dfs(i,k+1,val+nums[k][i])
    dfs(-1,0,0)
    return max[0]

def my2(nums:List[List[int]])->int:
    nums.insert(0,[0,0,0,0])
    for i in range(1,len(nums)):
        for j,val in enumerate(nums[i]):
            list = nums[i-1][:]
            list.pop(j)
            nums[i][j]=max(list)+val
    return (max(nums[-1]))

def practice(nums:List[List[int]])->int:
    nums.insert(0,[0,0,0,0])
    for i in range(1,len(nums)):
        for j,val in enumerate(nums[i]):
            list =nums[i-1][:]
            list.pop(j)
            nums[i][j]=max(list)+val
    return max(nums[-1])

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(list(map(int,input().split())))
    answer =my2(nums)
    print(answer)
