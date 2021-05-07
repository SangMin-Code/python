# 16569.py
import collections
import copy
import sys
from typing import List

sys.stdin = open('input/16569')


# def my(M:int,N:int,V:int,X:int,Y:int,board:List[List[int]],volcanoes:List[List[int]])->List[int]:
#     time = 0
#     dir = [[1,0],[0,-1],[-1,0],[0,1]]
#     volcanoes = collections.deque(volcanoes)
#     candidates = collections.deque()
#     candidates.append([X, Y, 0])
#     answer_height = board[X-1][Y-1]
#     answer_time = 0
#     while True:
#         #화산 폭발
#         next_volcanoes = collections.deque()
#         while volcanoes:
#             row,col,t = volcanoes.popleft()
#             if t>time:
#                 next_volcanoes.append([row,col,t])
#                 board[row-1][col-1]=-2
#             elif t==time:
#                 board[row-1][col-1]=-1
#                 for dr,dc in dir:
#                     nr, nc = row+dr,col+dc
#                     if 1<=nr<=M and 1<=nc<=N and board[row-1][col-1]>-2:
#                         next_volcanoes.append([nr,nc,t+1])
#         volcanoes =next_volcanoes
#         #이동가능
#         next_candidates = collections.deque()
#         while candidates:
#             row,col,t =candidates.popleft()
#             if t==time and board[row-1][col-1]>=0:
#                 if board[row-1][col-1] > answer_height:
#                     answer_height = board[row-1][col-1]
#                     answer_time = t
#                 board[row-1][col-1] = -1
#                 for dr, dc in dir:
#                     nr, nc = row + dr, col + dc
#                     if 1 <= nr <= M and 1 <= nc <= N \
#                             and board[nr - 1][nc - 1] >=0:
#                         next_candidates.append([nr,nc,t+1])
#         candidates = next_candidates
#         time += 1
#         if not candidates:
#             break
#     return [answer_height,answer_time]


def my(M:int,N:int,V:int,X:int,Y:int,board:List[List[int]],volcanoes:List[List[int]])->List[int]:

    dir = [[1,0],[0,-1],[-1,0],[0,1]]
    volcanoes = collections.deque(volcanoes)
    candidates = collections.deque()
    candidates.append([X, Y, 0])
    answer_height = board[X-1][Y-1]
    answer_time = 0

    #화산 폭발시간 판
    v_time = [[float('inf')]*N for _ in range(M)]
    after = []
    for r,c,t in volcanoes:
        after.append([r,c])
    time = 0
    while volcanoes:
        row,col,t = volcanoes.popleft()
        v_time[row-1][col-1] = min(v_time[row-1][col-1],t)
        for dr,dc in dir:
            nr,nc = row+dr,col+dc
            if 1<=nr<=M and 1<=nc<=N and v_time[nr-1][nc-1] > t+1:
                volcanoes.append([nr,nc,t+1])
        time+=1
    for r,c in after:
        v_time[r-1][c-1]=0

    time =0
    while candidates:
        row,col,t = candidates.popleft()
        if v_time[row-1][col-1] >t:
            if board[row-1][col-1]>answer_height:
                answer_height = board[row-1][col-1]
                answer_time = t
            v_time[row - 1][col - 1] = 0
            for dr, dc in dir:
                nr, nc = row + dr, col + dc
                if 1 <= nr <= M and 1 <= nc <= N and v_time[nr - 1][nc - 1] >t + 1:
                    candidates.append([nr, nc, t + 1])
        time += 1
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
    answer = my(M,N,V,X,Y,board,volcanoes)
    print(' '.join([str(i) for i in answer]))
