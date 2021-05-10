# 2630.py
import sys
from typing import List

sys.stdin = open('input/2630')


def my(n:int, board:List[List[int]])->List[int]:
    def dfs(sr,sc,l):
        cnt =[0,0]
        box_sum = 0
        for r in range(l):
            box_sum+=sum(board[sr+r][sc:sc+l])

        if box_sum == l**2:
            cnt[1]+=1
            return cnt
        elif box_sum==0:
            cnt[0]+=1
            return cnt
        else :
            next_l = l//2
            box1= dfs(sr,sc,next_l)
            box2= dfs(sr+next_l,sc,next_l)
            box3= dfs(sr,sc+next_l,next_l)
            box4= dfs(sr+next_l,sc+next_l,next_l)
            cnt[0] = box1[0]+box2[0]+box3[0]+box4[0]
            cnt[1] = box1[1]+box2[1]+box3[1]+box4[1]
            return cnt

    return dfs(0,0,n)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    board= []
    for _ in range(n):
        board.append(list(map(int,sys.stdin.readline().rstrip().split())))
    answer = my(n,board)
    for i in answer:
        print(i)
