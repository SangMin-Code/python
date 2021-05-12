# 6603.py
import sys
from typing import List

sys.stdin = open('input/6603')
import itertools

def my(nums:List[int])->List[List[int]]:
    candidates = nums[1:]
    result = itertools.combinations(candidates,6)
    answer =[]
    for i in result:
        answer.append(list(i))
    return answer

def my2(nums:List[int])->List[List[int]]:
    answer = []
    prev_list = []
    candidates = nums[1:]
    def dfs(c_list):
        if len(prev_list)==6:
            answer.append(prev_list[:])
        elif len(prev_list)<6:
            next_c=c_list[:]
            for i in range(len(c_list)):
                prev_list.append(c_list[i])
                dfs(next_c[i+1:])
                prev_list.pop()
    dfs(candidates)
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    nums = list(map(int,sys.stdin.readline().rstrip().split()))
    if nums[0]==0:
        print("stop")
    answer = my2(nums)
    for i in answer:
        print(' '.join([str(j) for j in i]))
    print()