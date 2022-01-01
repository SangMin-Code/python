import sys
from typing import List
sys.stdin = open('Programmers/level2/input/cutting_n_squre_array.txt')


def solution(n: int, left: int, right: int) -> List[int]:

    # matrix = [[0]*n for _ in range(n)]
    # for i in range(n):
    #     for j in range(i+1):
    #         matrix[i][j] = i+1
    #         matrix[j][i] = i+1
    # array = []
    # for i in matrix:
    #     array += i
    # return array[left:right+1]
    answer = []
    for i in range(left, right+1):
        answer.append(max(i % n, i//n)+1)
    return answer


TC = int(input())
for i in range(TC):
    n, left, right = map(int, input().split())
    result = solution(n, left, right)
    print(result)
