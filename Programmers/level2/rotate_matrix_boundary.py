import sys
from typing import List
sys.stdin = open('Programmers/level2/input/rotate_matrix_boundary.txt')


def solution(rows: int, columns: int, queries: List[List[int]]) -> List[int]:

    matrix = [[j+i*columns+1 for j in range(columns)] for i in range(rows)]
    result = [0]*len(queries)

    # x:row y:col

    for idx, query in enumerate(queries):
        x1, y1, x2, y2 = [i-1 for i in query]
        prev_rotate_num = -1
        present_rotate_num = -1

        min_num = rows*columns

        for i in range(x1, x2+1):
            min_num = min(min_num, matrix[i][y1], matrix[i][y2])
        for i in range(y1, y2+1):
            min_num = min(min_num, matrix[x1][i], matrix[x2][i])

        result[idx] = min_num

        # rotate x1 y1 to x1 y2
        prev_rotate_num = matrix[x1][y2]
        for i in range(y2, y1, -1):
            matrix[x1][i] = matrix[x1][i-1]

        # rotate x1 y2 to x2 y2
        present_rotate_num = matrix[x2][y2]
        for i in range(x2, x1, -1):
            matrix[i][y2] = matrix[i-1][y2]
        matrix[x1+1][y2] = prev_rotate_num
        prev_rotate_num = present_rotate_num

        # rotate x2 y2 to x2 y1
        present_rotate_num = matrix[x2][y1]
        for i in range(y1, y2):
            matrix[x2][i] = matrix[x2][i+1]
        matrix[x2][y2-1] = prev_rotate_num
        prev_rotate_num = present_rotate_num

        # rotate x2 y1 to x1 y1
        for i in range(x1, x2):
            matrix[i][y1] = matrix[i+1][y1]
        matrix[x2-1][y1] = prev_rotate_num

    return result


TC = int(input())
for i in range(TC):
    rows, columns = map(int, input().split())
    queries = [list(map(int, i.split())) for i in input().split(',')]
    result = solution(rows, columns, queries)
    print(result)
