#Q2.py
import sys
sys.stdin=open('input/Q2')
from typing import List

def my(s:str)->int:
    nums = []
    idx = -1
    for i,v in enumerate(s):
        if v.isdigit() and s[i+1].isdigit():
            nums.append(int(s[i:i+2]))
            idx+=1
        elif v.isdigit() and i >0 and s[i-1].isdigit():
            continue
        elif v.isdigit():
            nums.append(int(v))
            idx+=1
        else:
            if v=='S':
                nums[idx] = nums[idx]
            elif v=='D':
                nums[idx] = nums[idx]**2
            elif v=='T':
                nums[idx]= nums[idx]**3
            elif v == '#':
                nums[idx]=nums[idx]*(-1)
            elif v=='*':
                nums[idx]=nums[idx]*2
                if idx !=0:
                    nums[idx-1]=nums[idx-1]*2
    return sum(nums)

def solution(dartResult:str)->int:
    nums = [0]
    for s in dartResult:
        if s =='S':
            nums[-1]**=1
            nums.append(0)
        elif s =='D':
            nums[-1]**=2
            nums.append(0)
        elif s =='T':
            nums[-1]**=3
            nums.append(0)
        elif s =="*":
            #이전 값, 그 이전 값 모두 두 배 처리
            nums[-2]*=2
            if len(nums)>2:
                nums[-3]*=2
        elif s =='#':
            nums[-2]*=-1
        else :
            nums[-1] = nums[-1]*10 +int(s)
    return sum(nums)

TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    answer = my(s)
    print(answer)