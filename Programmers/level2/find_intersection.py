import sys
import itertools
from typing import List
sys.stdin = open('Programmers/level2/input/find_intersection.txt')


def solution(line: List[List[int]]) -> List[List[str]]:

    intersection_list = []

    line_combination = itertools.combinations(line, 2)

    min_x, min_y = float('inf'), float('inf')
    for line_1, line_2 in line_combination:
        a, b, e = line_1
        c, d, f = line_2
        if a*d-b*c == 0:
            continue
        else:
            i_x = (b*f-e*d)/(a*d-b*c)
            i_y = (e*c-a*f)/(a*d-b*c)
            if i_x.is_integer() and i_y.is_integer():
                min_x = min(min_x, int(i_x))
                min_y = min(min_y, int(i_y))
                if [int(i_x), int(i_y)] not in intersection_list:
                    intersection_list.append([int(i_x), int(i_y)])
    max_x, max_y = 0, 0
    for i in range(len(intersection_list)):
        intersection_list[i][0] -= min_x
        intersection_list[i][1] -= min_y
        max_x = max(max_x, intersection_list[i][0])
        max_y = max(max_y, intersection_list[i][1])

    if len(intersection_list) == 1:
        return ['*']
    else:
        matrix = [['.']*(max_x+1) for _ in range(max_y+1)]
        for x, y in intersection_list:
            matrix[max_y-y][x] = '*'
        for idx, row in enumerate(matrix):
            matrix[idx] = ''.join(row)
        return matrix


TC = int(input())
for i in range(TC):
    line = [list(map(int, i.split())) for i in input().split(',')]
    result = solution(line)
    print(result)
