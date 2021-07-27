# Q2.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(n:int,computers:List[List[int]])->int:
    dic = collections.defaultdict(list)
    visited = [False]*n
    cnt= 0

    for i,coms in enumerate(computers):
        for j in range(n):
            if i!=j and coms[j]==1:
                dic[i].append(j)
    def DFS(node):
        visited[node]=True
        for i in dic[node]:
            if not visited[i]:
                visited[i]=True
                DFS(i)
    for i in range(n):
        if not visited[i]:
            cnt+=1
        DFS(i)

    return cnt

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    computers = [list(map(int, i.split())) for i in input().split(',')]
    answer = my(n,computers)
    print(answer)
