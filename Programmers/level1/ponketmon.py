import sys
from typing import List

sys.stdin = open('Programmers/level1/input/ponketmon.txt')


def solution(nums: List[int]) -> int:
    # max_length = len(nums)//2
    # set_length = len(set(nums))

    # if set_length >= max_length:
    #     return max_length
    # else :
    #     return set_length

    return min(len(nums)//2, len(set(nums)))


TC = int(input())
for i in range(TC):
    result = solution(list(map(int, input().split())))
    print(result)
