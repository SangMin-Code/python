# 2447.py
import sys
from typing import List

sys.stdin = open('input/2447')
#???? 왜틀림
def my(n:int)->List[str]:
    board = [["*"]*n for _ in range(n)]
    def dfs(sr,sc,l):
        l = l//3
        for dr in range(l,2*l):
            for dc in range(l,2*l):
                board[sr+dr][sc+dc]=' '
        if l>1:
            dfs(sr,sc,l)
            dfs(sr,sc+l,l)
            dfs(sr,sr+2*l,l)
            dfs(sr+l,sc,l)

            dfs(sr+l,sc+2*l,l)
            dfs(sr+2*l,sc,l)
            dfs(sr+2*l,sc+l,l)
            dfs(sr+2*l,sc+2*l,l)
    dfs(0,0,n)
    return [''.join(i) for i in board]

def my2(n:int):
    board = [["*"]*n for _ in range(n)]
    cnt,m=0,n

    while m>1:
        m=m//3
        cnt+=1

    def star(a):
        idx = [i for i in range(n) if (i//3 **a)%3==1]
        for i in idx:
            for j in idx:
                board[i][j]=" "

    for c in range(cnt):
        star(c)

    print("\n".join([''.join([str(i) for i in row]) for row in board]))

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    answer = my2(n)
    # for i in answer:
    #     print(i)
