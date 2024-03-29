import sys
from typing import List

sys.stdin = open('Programmers/level1/input/number_and_word.txt')


def solution(s: str) -> str:

    if s.isdecimal():
        return int(s)

    table = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    for key, value in table.items():
        if key in s:
            s = s.replace(key, value)
    return int(s)


TC = int(input())
for i in range(TC):
    result = solution(input())
    print(result)
