#LCM_elelments.py
#https://programmers.co.kr/learn/courses/30/lessons/12953
import sys
sys.stdin=open('input/LCM_elelments')
from typing import List


# GCD: 최대공약수 greatest common divisor
# LCM : 최소공배수 Least common multiple  a,b의 LCM = a*b / GCD
def my(nums:List[int])->int:
    def GCD(a,b):
        #a,b = max(a,b),min(a,b)
        if a%b==0:
            return b
        return GCD(b,a%b)


    for i in range(1,len(nums)):
        nums[i] = nums[i-1] * nums[i] //GCD(nums[i-1],nums[i])
    return nums[-1]


TC = int(input())
for test_case in range(1,TC+1):
    nums = list(map(int,input().split()))
    answer =my(nums)
    print(answer)