# lock_and_key.py
import copy
import sys
from typing import List

sys.stdin = open('input/lock_and_key')


def my(key:List[List[int]], lock:List[List[int]])->bool:
    def lotation(board):
        n = len(board) - 1
        l_board = [[0]*(n+1) for i in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                l_board[j][n-i]=board[i][j]
        return l_board

    def check(key,lock):
        #expand -> key의 오른쪽 대각선 끝이 lock의 시작점일때 ~ key의 시작점이 lock의 오른쪽대각선 끝일때까지
        len_ex = len(lock) + (len(key)-1)*2
        expand_lock = [[0]*len_ex for _ in range(len_ex)]
        for i in range(len(lock)):
            for j in range(len(lock)):
                expand_lock[len(key)-1+i][len(key)-1+j] = lock[i][j]  #비교용 lock

        for i in range(len(key)+len(lock)-1):
            for j in range(len(key)+len(lock)-1):
                expand_key = [[0] * len_ex for _ in range(len_ex)]
                flag = True
                for k in range(len(key)):
                    for l in range(len(key)):
                        expand_key[i+k][j+l] = key[k][l]   #비교용 key
                for k in range(len(lock)):
                    for l in range(len(lock)):
                        if expand_key[len(key)-1+k][len(key)-1+l]+expand_lock[len(key)-1+k][len(key)-1+l]!=1: #비교
                            flag = False
                            break
                if flag : return True
        return False

    for _ in range(4):
        if check(key,lock):
            return True
        else :
            key = lotation(key)

    return False

def my2(key:List[List[int]], lock:List[List[int]])->bool:

    M,N= len(key),len(lock)

    def lotation(board):
        n = len(board)
        new_board = [[0]*n for i in range(n)]
        for i in range(n):
            for j in range(n):
                new_board[i][j]=board[j][n-1-i]
        return new_board

    def check(key,lock):
        len_ex = len(lock) + (len(key) - 1) * 2
        expand_lock = [[0] * len_ex for _ in range(len_ex)]
        for i in range(len(lock)):
            for j in range(len(lock)):
                expand_lock[len(key) - 1 + i][len(key) - 1 + j] = lock[i][j]

        for i in range(len(key) + len(lock) - 1):
            for j in range(len(key) + len(lock) - 1):
                expand_key = [[0] * len_ex for _ in range(len_ex)]
                flag = True
                for k in range(len(key)):
                    for l in range(len(key)):
                        expand_key[i + k][j + l] = key[k][l]
                for k in range(len(lock)):
                    for l in range(len(lock)):
                        if expand_key[len(key) - 1 + k][len(key) - 1 + l] + expand_lock[len(key) - 1 + k][
                            len(key) - 1 + l] != 1:  # 비교
                            flag = False
                            break
                if flag: return True
        return False

    for _ in range(4):
        if check(key,lock):
            return True
        else :
            key = lotation(key)
    return False

TC = int(input())
for test_case in range(1, TC + 1):
    key = [list(map(int,i.split()))for i in list(input().split(','))]
    lock = [list(map(int, i.split())) for i in list(input().split(','))]
    answer = my2(key,lock)
    print(answer)
