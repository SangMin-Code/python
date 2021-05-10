# 1780.py
import sys
from typing import List

sys.stdin = open('input/1780')

#시간초과
# def my(n:int, board:List[List[int]])->List[int]:
#     def dfs(sr,sc,l):
#         cnt =[0,0,0] # -1,0,1
#         flag = False
#         box_sum=0
#         for r in range(l):
#             box_sum+=sum(board[sr+r][sc:sc+l])
#             if board[sr+r][sc:sc+l].count(1) > 0 or board[sr+r][sc:sc+l].count(-1)>0:
#                 flag=True
#
#         if box_sum == l**2:
#             cnt[2]+=1
#             return cnt
#         elif box_sum == 0 and not flag:
#             cnt[1]+=1
#             return cnt
#         elif box_sum == -(l**2):
#             cnt[0]+=1
#             return cnt
#         else :
#             next_l = l//3
#             boxes = [[0,0],[0,next_l],[0,next_l*2],[next_l,0],[next_l,next_l],
#                      [next_l,next_l*2],[next_l*2,0],[next_l*2,next_l],[next_l*2,next_l*2]]
#             for dr,dc in boxes:
#                 box = dfs(sr+dr,sc+dc,next_l)
#                 cnt[0]+=box[0]
#                 cnt[1]+=box[1]
#                 cnt[2]+=box[2]
#             return cnt
#     return dfs(0,0,n)

def my(n:int, board:List[List[int]])->List[int]:
    cnt = [0, 0, 0]  # -1,0,1
    def dfs(sr, sc, l):
        global a, b, c
        num = board[sr][sc]
        for r in range(sr,sr+l):
            for c in range(sc,sc+l):
                if board[r][c]!=num:
                    for dr in range(3):
                        for dc in range(3):
                            dfs(sr+dr*l//3,sc+dc*l//3,l//3)
                    return
        if num==-1:
            cnt[0]+=1
        elif num==0:
            cnt[1]+=1
        else:
            cnt[2]+=1
    dfs(0,0,n)

    return cnt

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    board= []
    for _ in range(n):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    a,b,c =0,0,0
    answer = my(n,board)
    for i in answer:
        print(i)
