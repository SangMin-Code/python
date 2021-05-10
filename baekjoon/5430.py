# 5430.py
import collections
import sys
from typing import List

sys.stdin = open('input/5430')


#제출시 띄어쓰기 문제.
def my(command:str,n:int,nums:List[int])->List:
    nums = collections.deque(nums)
    if len(nums) < command.count("D"):
        return ["error"]
    is_reversed = False
    for i in command:
        if i =="R":
            is_reversed = not is_reversed
        elif i=="D":
            if nums:
                if is_reversed:
                    nums.pop()
                else :
                    nums.popleft()
    if is_reversed:
        return list(nums)[::-1]
    else:
        return list(nums)

def my2(command:str,n:int,nums:List[int])->List:
    left,right = 0,len(nums)
    is_reversed = False
    if len(nums)<command.count("D"):
        return ["error"]
    for i in command:
        if i =="R":
            is_reversed = not is_reversed
        elif i=="D":
            if is_reversed:
                right-=1
            else :
                left+=1
    if is_reversed:
        return nums[left:right][::-1]
    else :
        return nums[left:right]

TC = int(sys.stdin.readline().rstrip())
for test_case in range(1, TC + 1):
    command = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    nums = sys.stdin.readline().rstrip()
    if n>0:
        nums = list(map(int,nums[1:-1].split(",")))
    else:
        nums = []
    answer = my2(command,n,nums)

    if answer and answer[0]=="error":
        print("error")
    else :
        print(str(answer).replace(" ",""))

