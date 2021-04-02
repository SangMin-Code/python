#Q6.py
import sys
sys.stdin=open('input/Q6')
from typing import List

def my(m:int, n:int, board:List[List[str]])->int:
    changed_board = [[0]*m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            changed_board[j][m-i-1] = board[i][j]
    cnt = 0
    d = [[1,0],[1,1],[0,1],[0,0]]
    while True :
        point = []
        flag = False
        for i in range(n-1):
            for j in range(min(len(changed_board[i]),len(changed_board[i+1]))-1):
                if changed_board[i][j] == changed_board[i][j+1] \
                    == changed_board[i+1][j]==changed_board[i+1][j+1]:
                    point.append([i,j])
                    flag=True
        if not flag:
            break
        new_board = []
        for i,j in point:
            for x,y in d:
                if changed_board[i+x][j+y]!='0':
                    cnt+=1
                    changed_board[i+x][j+y]='0'

        for i in range(n):
            new_board.append(list(''.join(changed_board[i]).replace('0','')))
        changed_board=new_board
    return cnt

def solution(m:int, n:int, board:List[List[str]])->int:
    board = [list(x) for x in board]
    matched = True
    while matched:
        #1) 일치 여부 판별
        matched = []
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==\
                    board[i][j+1]==\
                    board[i+1][j+1]==\
                    board[i+1][j] !='#':
                    matched.append([i,j])
        #2) 일치한 위치 삭제
        for i,j in matched:
            board[i][j] = board[i][j+1]=board[i+1][j+1]=board[i+1][j]='#'
        #3) 빈공간 블럭 처리
        for _ in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board[i+1][j]=='#':
                        board[i+1][j],board[i][j]=board[i][j],'#'
    return sum(x.count('#') for x in board)


TC = int(input())
for test_case in range(1,TC+1):
    m,n = map(int,input().split())
    board =[]
    for _ in range(m):
        board.append(input())
    answer =my(m,n,board)
    print(answer)