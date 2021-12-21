import sys
from typing import List

sys.stdin = open('hackerRank/easy/input/solve_me_first.txt')


def solution(a: int, b: int) -> int:
    return a+b


TC = int(input())

for i in range(TC):
    a, b = map(int, input().split())
    result = solution(a, b)
    print(result)
