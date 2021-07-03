# 1806.py
import sys
from typing import List

sys.stdin = open('input/1806')


def my(N:int,S:int,nums:List[int])->int:
    left, right = 0, 0
    tmp_sum = 0
    min_length = int('float')

    while True:
        if tmp_sum >= S:
            min_length = min(min_length, right - left)
            tmp_sum -= nums[left]
            left += 1

        elif right == N:
            break

        else:
            tmp_sum += nums[right]
            right += 1

    if min_length == int('float'):
        return 0
    else:
        return min_length


TC = int(input())
for test_case in range(1, TC + 1):
    N,S = map(int,input().split())
    nums = list(map(int,input().split()))

    answer = my(N,S,nums)
    print(answer)
