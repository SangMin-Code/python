# 1520.py
import sys
from typing import List

sys.stdin = open('input/1520')


def my(r:int,c:int,board:List[List[int]])->int:
    di = [[1,0],[0,1],[0,-1],[-1,0]]
    dp = [[-1]*c for _ in range(r)]
    def DFS(ir,ic):
        if [ir,ic] == [r-1,c-1]:
            return 1
        elif dp[ir][ic]==-1:
            dp[ir][ic]=0
            for dr,dc in di:
                nr,nc = ir+dr,ic+dc
                if 0<=nr<r and 0<=nc<c and board[ir][ic]>board[nr][nc]:
                    dp[ir][ic]+=DFS(nr,nc)
        return dp[ir][ic]
    return DFS(0,0)

TC = int(input())
for test_case in range(1, TC + 1):
    r,c = map(int,sys.stdin.readline().rstrip().split())
    board = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(r)]
    answer = my(r,c,board)
    print(answer)
