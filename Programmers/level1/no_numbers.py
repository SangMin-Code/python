import sys
from typing import List

sys.stdin = open('Programmers/level1/input/no_numbers.text')


def solution(numbers: List[int]):
    answer = 0
    numbers_all = set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
    numbers_set = set(numbers)
    answer = sum(numbers_all-numbers_set)
    return answer


TC = int(input())
for i in range(TC):
    numbers = list(map(int, input().split()))
    result = solution(numbers)
    print(result)
