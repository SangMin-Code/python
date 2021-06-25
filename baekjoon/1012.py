# 1012.py
import sys
from typing import List
import collections

sys.stdin = open('input/1012')

def my(M:int,N:int, board:List[List[int]])->List[int]:

    answer = 0

    def BFS(point):
        queue = collections.deque()
        queue.append(point)
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        while queue:
            row,col = queue.popleft()
            board[row][col]=0
            for dr,dc in dir:
                nr,nc = row+dr,col+dc
                if 0<=nr<N and 0<=nc<M and board[nr][nc]!=0:
                    queue.append([nr,nc])
                    board[nr][nc]=0

    for r in range(N):
        for c in range(M):
            if board[r][c]!=0:
                answer+=1
                BFS([r,c])

    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    M,N,K = map(int,input().split())
    board = [[0]*(M) for _ in range(N)]
    for _ in range(K):
        c,r = map(int,input().split())
        board[r][c]=1
    answer = my(M,N,board)
    print(answer)