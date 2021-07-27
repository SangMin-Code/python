# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(numbers:List[int],target:int)->int:
    def dfs(sum,k):
        if k == len(numbers):
            if sum ==target:
                return 1
            else :
                return 0
        else :
            return dfs(sum+numbers[k],k+1)+dfs(sum-numbers[k],k+1)
    return dfs(0,0)

def my2(numbers:List[int],target:int)->int:
    def dfs(sum,k):
        if k==len(numbers):
            if sum==target:
                return 1
        else:
            return dfs(sum+numbers[k],k+1)+dfs(sum-numbers[k],k+1)
    return dfs(0,0)



TC = int(input())
for test_case in range(1, TC + 1):
    numbers = list(map(int,input().split()))
    target = int(input())
    answer = my(numbers,target)
    print(answer)
