import sys
from typing import List

sys.stdin = open('Programmers/level1/input/number_with_remainder_1.txt')


def solution(n: int) -> int:
    for i in range(1, n):
        if n % i == 1:
            return i


TC = int(input())
for i in range(TC):
    result = solution(int(input()))
    print(result)
