# 1300.py
import sys
from typing import List

sys.stdin = open('input/1300')


def my(N:int, k:int)->int:
    left =1
    right = k
    result = 0
    while left<=right:
        mid = left+(right-left)//2
        cnt = 0
        for i in range(1,N+1):
            cnt+=min(mid//i,N)
        if(cnt>=k):
            result =mid
            right = mid-1
        else :
            left = mid+1
    return result

TC = int(input())
for test_case in range(1, TC + 1):
    N = int(sys.stdin.readline().rstrip())
    k = int(sys.stdin.readline().rstrip())
    answer = my(N,k)
    print(answer)
