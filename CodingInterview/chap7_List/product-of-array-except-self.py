#product-of-array-except-self.py

import  sys
from typing import List
sys.stdin=open('input/product-of-array-except-self')

def my(nums:List[int])->List[int]:
    '''
    #나눗셈을 이용할 경우 O(n)
    val =1
    answer =[]
    for i in nums:
        val*=i
    for i in nums:
        answer.append(val/i)
        val*=i
    return answer
    '''


def productExceptSelf(nums:List[int])->List[int]:
    out=[]
    p=1
    #왼쪽 곱셈
    for i in range(0,len(nums)):
        out.append(p)
        p=p*nums[i]
    p=1
    #오른쪽 값을 왼쪽 곱셈 결과에 차례대로 곱셈
    for i in range(len(nums)-1, 0-1, -1):
        out[i]=out[i]*p
        p=p*nums[i]
    return out

nums = list(map(int,input()))

