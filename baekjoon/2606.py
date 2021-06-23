# 2606.py
import collections
import sys
from typing import List

sys.stdin = open('input/2606')


def my(n:int,m:int,edges:List[List[int]])->int:
    dic = collections.defaultdict(list)
    for n1,n2 in edges:
        dic[n1].append(n2)
        dic[n2].append(n1)
    visited = [0]*(n+1)
    queue = collections.deque()
    queue.append(1)

    while queue:
        node = queue.popleft()
        visited[node]=1
        for next_node in dic[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node]=1

    return sum(visited)-1



TC = int(input())
for test_case in range(1, TC + 1):
    n = int(input())
    m = int(input())
    edges = [list(map(int,input().split())) for _ in range(m)]
    answer = my(n,m,edges)
    print(answer)
