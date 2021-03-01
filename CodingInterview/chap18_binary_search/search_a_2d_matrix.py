import sys
sys.stdin = open('input/search_a_2d_matrix')
from typing import List

def searchMatrix(matrix:List[List[int]], target:int)->bool:
    if not matrix:
        return False

    row = 0
    col = len(matrix[0])-1

    while row <=len(matrix)-1 and col>=0:
        value = matrix[row][col]
        if target == value:
            return True
        elif target < value:
            col-=1
        elif target >value:
            row+=1
    return False

def pythonic_way(matrix, target):
    return any(target in row for row in matrix)



n = int(input())
matrix = []
target = int(input())
for _ in range(n):
    low = list(map(int,input().split()))
    matrix.append(low)
