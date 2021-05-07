# 16569.py
import collections
import copy
import sys
from typing import List

sys.stdin = open('input/16569')


def my(M:int,N:int,V:int,X:int,Y:int,board:List[List[int]],volcanoes:List[List[int]])->List[int]:

    time = 0
    dir = [[1,0],[0,-1],[-1,0],[0,1]]
    volcanoes = collections.deque(volcanoes)
    candidates = collections.deque()
    candidates.append([X, Y, 0])
    answer_height = board[X-1][Y-1]
    answer_time = 0

    while True:
        #화산 폭발
        next_volcanoes = collections.deque()
        while volcanoes:
            row,col,t = volcanoes.popleft()
            if t>time:
                board[row-1][col-1]=-1
                next_volcanoes.append([row,col,t])
            elif t==time:
                board[row-1][col-1]=-1
                for dr,dc in dir:
                    nr, nc = row+dr,col+dc
                    if 1<=nr<=M and 1<=nc<=N and board[nr-1][nc-1]!=-1:
                        next_volcanoes.append([nr,nc,t+1])
        volcanoes =next_volcanoes

        #이동가능
        next_candidates = collections.deque()
        while candidates:
            row,col,t =candidates.popleft()
            if t==time and board[row-1][col-1]>=0:
                if board[row-1][col-1] > answer_height:
                    answer_height = board[row-1][col-1]
                    answer_time = t
                board[row-1][col-1] = -2
                for dr, dc in dir:
                    nr, nc = row + dr, col + dc
                    if 1 <= nr <= M and 1 <= nc <= N \
                            and board[nr - 1][nc - 1] >=0:
                        next_candidates.append([nr,nc,t+1])
            elif t>time:
                next_candidates.append([row,col,t])
        candidates = next_candidates

        time += 1

        if not candidates:
            break

    return [answer_height,answer_time]

TC = int(input())
for test_case in range(1, TC + 1):
    M,N,V = map(int,sys.stdin.readline().rstrip().split())
    X,Y = map(int,sys.stdin.readline().rstrip().split())
    board = []
    for _ in range(M):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    volcanoes=[]
    for _ in range(V):
        volcanoes.append(list(map(int,sys.stdin.readline().rstrip().split())))
        # 화산 위치 board[i][j] = -1
        # x,y = volcanoes[-1][0],volcanoes[-1][1]
        # board[x-1][y-1]=-1
    answer = my(M,N,V,X,Y,board,volcanoes)
    print(' '.join([str(i) for i in answer]))
