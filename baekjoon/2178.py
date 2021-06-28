# 2178.py
import collections
import sys
from typing import List

sys.stdin = open('input/2178')


def my(N:int,M:int,board:List[str])->int:
    answer = 0
    queue = collections.deque()
    queue.append([0,0,1])
    visited = [[0]*M for _ in range(N)]
    dir = [[0,1],[1,0],[-1,0],[0,-1]]

    while queue:
        r,c,cnt = queue.popleft()
        visited[r][c]=cnt
        for dr,dc in dir:
            nr,nc = r+dr, c+dc
            if 0<=nr<N and 0<=nc<M and not visited[nr][nc] and board[nr][nc]!='0':
                visited[nr][nc]=cnt+1
                queue.append([nr,nc,cnt+1])

    return visited[-1][-1]


TC = int(input())
for test_case in range(1, TC + 1):
    N,M = map(int,input().split())
    board = [input() for _ in range(N)]
    answer = my(N,M,board)
    print(answer)
