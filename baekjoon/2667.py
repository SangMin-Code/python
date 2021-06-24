# 2667.py
import collections
import sys
from typing import List

sys.stdin = open('input/2667')


def my(n:int, board:List[str])->List[int]:
    visited = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            visited[r][c]=int(board[r][c])

    answer = 0
    count = []

    def BFS(point):
        queue = collections.deque()
        queue.append(point)
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        count.append(0)
        while queue:
            row,col = queue.popleft()
            visited[r][c]=0
            count[-1]+=1
            for dr,dc in dir:
                nr,nc = row+dr,col+dc
                if 0<=nr<n and 0<=nc<n and visited[nr][nc]!=0:
                    queue.append([nr,nc])
                    visited[nr][nc]=0

    for r in range(n):
        for c in range(n):
            if visited[r][c]!=0:
                answer+=1
                BFS([r,c])

    return [answer]+sorted(count)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    board = [input() for _ in range(n)]
    answer = my(n,board)

    for i in answer:
        print(i)
