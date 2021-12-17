import sys
from typing import List
sys.stdin = open('Programmers/level1/input/min_length_rectangle.txt')


def solution(sizes: List[List[int]]) -> int:
    col, row = 0, 0
    for size in sizes:
        size.sort()
        col = max(size[0], col)
        row = max(size[1], row)
    return col*row


TC = int(input())
for i in range(TC):
    sizes = [list(map(int, i.split())) for i in list(input().split(','))]
    result = solution(sizes)
    print(result)
