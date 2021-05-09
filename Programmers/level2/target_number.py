# target_number.py
import sys
from typing import List

sys.stdin = open('input/target_number')


def my(numbers:List[int],target:int)->int:
    def dfs(idx,val):
        if idx==len(numbers):
            if val == target:
                return 1
            else :
                return 0
        return dfs(idx+1,val+numbers[idx])+dfs(idx+1,val-numbers[idx])
    return dfs(0,0)

TC = int(input())
for test_case in range(1, TC + 1):
    numbers = list(map(int,input().split()))
    target = int(input())
    answer = my(numbers,target)
    print(answer)
