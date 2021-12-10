# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3
# 124_numbers.py
from typing import List
import sys
sys.stdin = open('input/124_numbers')


def my(n: int) -> int:
    answer = ''
    rest = 0
    while n > 0:
        rest = n % 3
        n //= 3
        if rest == 0:
            rest = 4
            n -= 1
        answer = str(rest)+answer
    return answer


def practice(n: int) -> str:
    answer = ''
    while n > 0:
        rest = n % 3
        n /= 3
        if rest == 0:
            rest = 4
            n -= 1
        answer = str(rest)+answer
    return answer


TC = int(input())
for test_case in range(1, TC+1):
    n = int(input())
    answer = my(n)
    print(answer)
