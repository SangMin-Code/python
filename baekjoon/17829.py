# 17829.py
import sys
from typing import List

sys.stdin = open('input/17829')


def my(n:int, board:List[List[int]])->int:

    def dfs(n,board):
        if n==2:
            temp = [board[0][0],board[1][0],board[0][1],board[1][1]]
            temp = sorted(temp)
            return temp[2]

        n//=2
        new_board = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                temp = [board[2*i][2*j],board[2*i+1][2*j],board[2*i][2*j+1],board[2*i+1][2*j+1]]
                temp =sorted(temp)
                new_board[i][j]=temp[2]
        return dfs(n,new_board)

    return dfs(n,board)

TC = int(input())
for test_case in range(1, TC + 1):
    n= int(sys.stdin.readline().rstrip())
    board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(n)]
    answer = my(n,board)
    print(answer)
