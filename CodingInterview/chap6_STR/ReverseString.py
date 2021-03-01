#ReverseString
import sys
from typing import List

sys.stdin = open('input/ReverseString','r')

def my(strs : List[str])->None:
    strs.reverse()

def twoPoint(s:List[str])->None:
    left, right = 0, len(s)-1
    while left<right:
        s[left],s[right] = s[right],s[left]
        left+=1
        right-=1

TC=int(input())
for test_case in range(1,TC+1):
    strs = list(input().split())
    #my(strs)
    twoPoint(strs)
    print(strs)