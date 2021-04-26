# N_Queen.py
#https://programmers.co.kr/learn/courses/30/lessons/12952#
import copy
import sys
from typing import List

sys.stdin = open('input/N_Queen')
'''
    empty_board = [[0]*n for _ in range(n)]
    answer = []
    def DFS(board,row):
        if row==n:
            answer.append(board[:])
        elif row < n:
            for col in range(n):
                if board[row][col] !=1 :
                    next_board = copy.deepcopy(board)
                    for i in range(n-row):
                        next_board[row + i][col] = 1  # 열
                        if row+i <n and col+i<n:
                            next_board[row+i][col+i]=1 #오른쪽아래대각선
                        if row+i<n and col-i >-1:
                            next_board[row+i][col-i]=1 #왼쪽아래대각선
                    DFS(next_board,row+1)
    DFS(empty_board,0)
    return len(answer)
    #timeout
'''

def my(n:int)->int:
    def DFS(queen, row, n):
        count = 0
        if n == row :
            return 1
        elif row<n :
            for col in range(n):
                queen[row]=col
                flag = True
                for i in range(row):
                    if queen[row]==queen[i] or abs(queen[i]-queen[row]) == row -i:
                        flag = False
                        break
                if flag:
                    count += DFS(queen,row+1,n)
        return count
    return DFS([0]*n,0,n)

    #반복문으로 만들려면???


TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    answer = my(n)
    print(answer)
