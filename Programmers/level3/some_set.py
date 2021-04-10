#some_set.py
import sys
sys.stdin=open('input/some_set')
from typing import List
import math

def my(n:int,s:int)->List[int]:
    if n > s:
        return [-1]
    answer = []
    for i in range(n):
        answer.append(math.ceil(s / (n - i)))
        s -= math.ceil(s / (n - i))
    return sorted(answer)

TC = int(input())
for test_case in range(1,TC+1):
    n,s = map(int,input().split())
    answer = my(n,s)
    print(answer)