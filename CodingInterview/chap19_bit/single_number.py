import sys
sys.stdin = open('input/single_number')
import collections
from typing import List
def my(nums:List[int])->int:
    elements = collections.Counter(nums)
    for i in elements:
        if elements[i]<2:
            print(i)

def single_number(nums:List[int])->int:
    result = 0
    for num in nums:
        result^=num
        print(result)
    return result

    #TODO  ^ 연산시 같은 숫자는 0
    # ex) 1^3 = 4 , 1^3^3=1

TC = int(input())
for test_case in range(1,TC+1):
    nums = list(map(int,input().split()))
    #my(nums)
    single_number(nums)