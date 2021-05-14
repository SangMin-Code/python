# 9184.py
import collections
import sys
from typing import List

sys.stdin = open('input/9184')


def my(a:int,b:int,c:int):
    vals = collections.defaultdict()
    def w(a,b,c):
        if (a,b,c) in vals:
            return vals[(a,b,c)]

        if a>20 or b>20 or c>20 :
            return w(20,20,20)

        if a<=0 or b<=0 or c<=0:
            if (a,b,c) not in vals:
                vals[(a,b,c)]=1
            return vals[(a, b, c)]

        if a<b and b<c :
            if (a,b,c) not in vals:
                vals[(a,b,c)]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
            return vals[(a, b, c)]

        if (a,b,c) not in vals:
            vals[(a, b, c)] =w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
            return vals[(a,b,c)]

    return w(a,b,c)

def my2(a:int,b:int,c:int):
    max = 21
    board = [[[0]*max for _ in range(max)] for _ in range(max)]

    def w(a,b,c):
        if a<=0 or b<=0 or c<=0:
            return 1
        if a>20 or b>20 or c>20:
            return w(20,20,20)

        if board[a][b][c]:
            return board[a][b][c]

        if a<b<c:
            board[a][b][c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
            return board[a][b][c]
        board[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
        return board[a][b][c]
    return w(a,b,c)

# def w(a, b, c):
#     if a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#
#     if dp[a][b][c] :
#         return dp[a][b][c]
#
#     if a<b<c :
#         dp[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
#     else:
#         dp[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
#
#     return dp[a][b][c]
#
#
#
# dp = [[[0 for _ in range(21)] for _ in range (21)] for _ in range (21)]
# while True:
#     a,b,c = map(int, input().split())
#     if a==-1 and b==-1 and c==-1:
#         break
#     print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))


TC = int(input())
for test_case in range(1, TC + 1):
    a,b,c = map(int,sys.stdin.readline().rstrip().split())
    answer = my2(a,b,c)
    print("w({}, {}, {}) = {}".format(a,b,c,answer))
