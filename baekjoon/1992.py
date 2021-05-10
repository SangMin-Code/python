# 1992.py
import sys
from typing import List

sys.stdin = open('input/1992')

def my(n:int, board:List[List[int]])->str:
    answer =[]
    def dfs(sr,sc,l):
        box_sum = 0
        for r in range(l):
            box_sum+=sum(board[sr+r][sc:sc+l])

        if box_sum == l**2:
            answer.append("1")

        elif box_sum==0:
            answer.append("0")

        else :
            next_l = l//2
            answer.append("(")
            dfs(sr,sc,next_l)
            dfs(sr,sc+next_l,next_l)
            dfs(sr + next_l, sc, next_l)
            dfs(sr+next_l,sc+next_l,next_l)
            answer.append(")")
            return

    dfs(0,0,n)
    return ''.join(answer)

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    board= []
    for _ in range(n):
        temp= []
        for i in sys.stdin.readline().rstrip():
            temp.append(int(i))
        board.append(temp)

    answer = my(n,board)
    print(answer)
