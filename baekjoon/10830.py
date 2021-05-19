# 10830.py
import sys
from typing import List

sys.stdin = open('input/10830')


def my(N:int,B:int,matrix:[List[List[int]]])->List[List[int]]:

    def multiple(a:List[List[int]],b:List[List[int]]):
        r,c,e = len(a),len(b[0]),len(b)
        m = [[0]*c for _ in range(r)]
        for i in range(N):
            for j in range(N):
                for l in range(e):
                    m[i][j]+=a[i][l]*b[l][j]
                m[i][j]%=1000

        return m
    i_matrix = [[1 if i==j else 0 for i in range(N)] for j in range(N)]

    def divide(m, ex):
        if ex==1:
            return multiple(m,i_matrix)
        elif ex==2:
            return multiple(m,m)
        else :
            tmp = divide(m,ex//2)
            if ex%2==0:
                return multiple(tmp,tmp)
            else:
                return multiple(multiple(tmp,tmp),m)

    return divide(matrix,B)

TC = int(input())
for test_case in range(1, TC + 1):
    N,B = map(int,sys.stdin.readline().rstrip().split())
    matrix = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
    answer = my(N,B,matrix)
    for i in answer:
        print(' '.join([str(j) for j in i]))
