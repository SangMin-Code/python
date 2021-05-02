# 1874.py
import sys
from typing import List

sys.stdin = open('input/1874')

def my(n:int,nums:List[int]):
    p_num, n_idx = 1,0
    stack = []
    answer = []
    for i in nums:
        while p_num<=i:
            stack.append(p_num)
            p_num += 1
            answer.append('+')
        if stack.pop()!=i:
            return ['NO']
        else :
            answer.append('-')
    return answer

    '''        
    while True:
        if len(stack)==0:
            if n == n_idx:
                return answer
            else :
                stack.append(p_num)
                answer.append('+')
                p_num+=1
        else :
            if stack[-1]==nums[n_idx]:
                answer.append('-')
                n_idx+=1
                stack.pop()
            elif stack[-1]<nums[n_idx]:
                if p_num > nums[n_idx]:
                    return ['NO']
                while stack[-1]<nums[n_idx]:
                    answer.append('+')
                    stack.append(p_num)
                    p_num+=1
            elif stack[-1]>nums[n_idx]:
                while len(stack)>0 and stack[-1]>nums[n_idx]:
                    answer.append('-')
                    stack.pop()
                if len(stack)==0:
                    return ['NO']
    '''
TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    nums = []
    for _ in range(n):
        nums.append(int(sys.stdin.readline().rstrip()))
    list =my(n,nums)
    for i in list:
        print(i)
