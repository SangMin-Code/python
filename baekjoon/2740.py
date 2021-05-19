# 2740.py
import sys
from typing import List

sys.stdin = open('input/2740')


def my(matrix_A:List[List[int]],matrix_B:List[List[int]])->List[List[int]]:
    r,c = len(matrix_A),len(matrix_B[0])
    matrix = [[0]*c for _ in range(r)]

    for i in range(r):
        for j in range(c):
            for k in range(len(matrix_B)):
                matrix[i][j]+=matrix_A[i][k]*matrix_B[k][j]
    return matrix




TC = int(input())
for test_case in range(1, TC + 1):
    N_A,M_A = map(int,sys.stdin.readline().rstrip().split())
    matrix_A = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N_A)]
    M_B,K_B = map(int,sys.stdin.readline().rstrip().split())
    matrix_B = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(M_B)]
    answer = my(matrix_A,matrix_B)
    for i in answer:
        print(' '.join([str(j) for j in i]))
