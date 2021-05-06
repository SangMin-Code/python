# 16920.py
import sys
from typing import List

sys.stdin = open('input/16920')
import collections

def my(N:int,M:int,P:int,p_s:List[int],board:List[List[str]])->List[str]:

    castle = [[] for _ in range(P+1)] # 플레이어가 가진 출발판대기들
    dir = [[0,1],[1,0],[0,-1],[-1,0]]
    block_cnt = [0]*(P+1)

    for i in range(N):
        for j in range(M):
            if board[i][j].isdigit():
                castle[int(board[i][j])].append([i,j,p_s[int(board[i][j])-1]])  #출발 위치
                block_cnt[int(board[i][j])]+=1

    while True:
        flag = False
        for idx, blocks in enumerate(castle):
            queue = collections.deque(blocks)
            new_blocks = []
            while queue:
                r,c,move_cnt = queue.popleft()
                if move_cnt==0:
                    new_blocks.append([r,c,p_s[idx-1]])
                elif move_cnt>0:
                    for dr,dc in dir:
                        n_r,n_c = r+dr,c+dc
                        if 0<=n_r<N and 0<=n_c<M and board[n_r][n_c]=='.':
                            queue.append([n_r,n_c,move_cnt-1])
                            board[n_r][n_c]=idx
                            block_cnt[idx]+=1
                            flag=True
            castle[idx]=new_blocks[:]
        if not flag:
            break
    return block_cnt[1:]



TC = int(input())
for test_case in range(1, TC + 1):
    N,M,P = map(int,sys.stdin.readline().rstrip().split()) #행, 열, 플레이어 수
    p_s = list(map(int,sys.stdin.readline().split()))    # i번째 플레이어가 가진 확장 가능 이동범위

    board = []  #판
    for _ in range(N):
        temp= []
        for i in sys.stdin.readline().rstrip():
            temp.append(i)
        board.append(temp)
    answer = my(N,M,P,p_s,board)
    print(' '.join([str(i) for i in answer]))
