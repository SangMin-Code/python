import collections
import sys
from typing import List

sys.stdin = open('Programmers/level2/input/light_path_cycle.txt')


def solution(grid: List[str]) -> List[int]:
    result = []

    dic_s = {'top': [-1, 0], 'bottom': [1, 0],
             'left': [0, -1], 'right': [0, 1]}

    dic_l = {'top': [0, -1], 'bottom': [0, 1],
             'left': [1, 0], 'right': [-1, 0]}
    change_l = {'top': 'left', 'bottom': 'right',
                'left': 'bottom', 'right': 'top'}
    dic_r = {'top': [0, 1], 'bottom': [0, -1],
             'left': [-1, 0], 'right': [1, 0]}
    change_r = {'top': 'right', 'bottom': 'left',
                'left': 'top', 'right': 'bottom'}

    matrix = [[str(i+1+(j)*(len(grid)+2)) for i in range(len(grid)+2)]
              for j in range(len(grid)+2)]

    candidate = []

    for row_idx, row in enumerate(grid):
        for col_idx, box in enumerate(row):
            matrix[row_idx+1][col_idx+1] = box

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            if matrix[row][col].isalpha():
                if matrix[row][col-1].isdecimal():
                    candidate.append([[row, col-1], 'right'])
                if matrix[row][col+1].isdecimal():
                    candidate.append([[row, col+1], 'left'])
                if matrix[row+1][col].isdecimal():
                    candidate.append([[row+1, col], 'top'])
                if matrix[row-1][col].isdecimal():
                    candidate.append([[row-1, col], 'bottom'])

    while candidate:
        start, direction = candidate.pop()
        length = 0
        pr, pc = start
        d = direction
        next_pr, next_pc = pr+dic_s[d][0], pc+dic_s[d][1]

        while next_pr != pr or next_pc != pc or d != direction:
            if matrix[next_pr][next_pc] == 'S':
                length += 1
                next_pr += dic_s[d][0]
                next_pc += dic_s[d][1]
            elif matrix[next_pr][next_pc] == 'L':
                length += 1
                next_pr += dic_l[d][0]
                next_pc += dic_l[d][1]
                d = change_l[d]
            elif matrix[next_pr][next_pc] == 'R':
                length += 1
                next_pr += dic_r[d][0]
                next_pc += dic_r[d][1]
                d = change_r[d]
            else:
                next_pr, next_pc = (next_pr +
                                    dic_s[d][0]) % (len(grid)+2), (next_pc+dic_s[d][1]) % (len(grid)+2)
            if [[next_pr, next_pc], d] in candidate:
                candidate.remove([[next_pr, next_pc], d])
        result.append(length)
    return result


def practice(grid: List[str]) -> List[int]:
    paths = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    info = {'S': {(1, 0): [1, 0], (-1, 0): [-1, 0], (0, 1): [0, 1], (0, -1): [0, -1]},
            'L': {(1, 0): [0, 1], (-1, 0): [0, -1], (0, 1): [-1, 0], (0, -1): [1, 0]},
            'R': {(1, 0): [0, -1], (-1, 0): [0, 1], (0, 1): [1, 0], (0, -1): [-1, 0]}}
    answers = []
    visited = set()
    length = len(grid)

    for i in range(length):
        for j in range(length):
            for path in paths:
                traced = set()
                num = 0
                stack = [[i, j]+path]
                while stack:
                    tmp = stack.pop()
                    if tuple(tmp) in traced:
                        continue
                    if tuple(tmp) in visited:
                        num = 0
                        break
                    visited.add(tuple(tmp))
                    traced.add(tuple(tmp))
                    cur = tmp[:2]
                    path = tmp[2:]
                    next_block = [(cur[0]+path[0]) % length,
                                  (cur[1]+path[1]) % length]
                    next_path = info[grid[next_block[0]]
                                     [next_block[1]]][tuple(path)]
                    stack.append(next_block+next_path)
                    num += 1
                if num != 0:
                    answers.append(num)
    return sorted(answers)


def solution(grid):
    paths = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    info = {'S': {(1, 0): [1, 0], (-1, 0): [-1, 0], (0, 1): [0, 1], (0, -1): [0, -1]},
            'L': {(1, 0): [0, 1], (-1, 0): [0, -1], (0, 1): [-1, 0], (0, -1): [1, 0]},
            'R': {(1, 0): [0, -1], (-1, 0): [0, 1], (0, 1): [1, 0], (0, -1): [-1, 0]}}
    answer = []
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for path in paths:
                traced = set()
                num = 0
                stack = [[i, j]+path]
                while stack:
                    tmp = stack.pop()
                    if tuple(tmp) in traced:
                        continue
                    if tuple(tmp) in visited:
                        num = 0
                        break
                    visited.add(tuple(tmp))
                    traced.add(tuple(tmp))
                    cur = tmp[:2]
                    path = tmp[2:]
                    next_block = [(cur[0]+path[0]) % len(grid),
                                  (cur[1]+path[1]) % len(grid[0])]
                    next_path = info[grid[next_block[0]]
                                     [next_block[1]]][tuple(path)]
                    stack.append(next_block+next_path)
                    num += 1
                if num != 0:
                    answer.append(num)
    return sorted(answer)


TC = int(input())
for i in range(TC):
    grid = list(input().split())
    result = solution(grid)
    print(result)
