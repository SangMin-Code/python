import sys
from typing import List
sys.stdin = open('Programmers/level2/input/keep_distance.txt')


def solution(places: List[List[str]]) -> List[int]:
    # 맨해튼거리: |r1-r2|+|c1-c2| 가 2 이하가 되지않도록,
    # 파티션이면 ok
    result = [0]*len(places)
    for idx, place in enumerate(places):
        result[idx] = check(place)
    return result


def check(place: List[str]) -> int:
    PERSON, OPEN, PARTITION = 'P', 'O', 'X'
    LENGTH = 5
    for row_idx, row in enumerate(place):
        for col_idx, col in enumerate(row):
            if place[row_idx][col_idx] == PERSON:
                if col_idx+1 < LENGTH:
                    if place[row_idx][col_idx+1] == PERSON:
                        return 0
                if row_idx+1 < LENGTH:
                    if place[row_idx+1][col_idx] == PERSON:
                        return 0
                if col_idx+2 < LENGTH:
                    if place[row_idx][col_idx+2] == PERSON and place[row_idx][col_idx+1] == OPEN:
                        return 0
                if row_idx+2 < LENGTH:
                    if place[row_idx+2][col_idx] == PERSON and place[row_idx+1][col_idx] == OPEN:
                        return 0
                if col_idx+1 < LENGTH and row_idx-1 >= 0:
                    if (place[row_idx-1][col_idx] == OPEN or place[row_idx][col_idx+1] == OPEN) and place[row_idx-1][col_idx+1] == PERSON:
                        return 0
                if col_idx+1 < LENGTH and row_idx+1 < LENGTH:
                    if (place[row_idx+1][col_idx] == OPEN or place[row_idx][col_idx+1] == OPEN) and place[row_idx+1][col_idx+1] == PERSON:
                        return 0
    return 1


TC = int(input())
for i in range(TC):
    places = [list(i.split()) for i in input().split(',')]
    result = solution(places)
    print(result)
