# 1260.py
import sys
from typing import List

sys.stdin = open('input/1260')


def my(N:int,M:int,V:int,in_edge:List[List[int]])->List[List[int]]:
    edges = [[]*(N+1) for _ in range(N+1)]
    for e1,e2 in in_edge:
        edges[e1].append(e2)
        edges[e2].append(e1)
    for i in range(1,N+1) :
        edges[i]=sorted(edges[i])
    answer = [[],[]]
    stack = []
    visited = []
    stack.append(V)

    def DFS(node):
        visited.append(node)
        answer[0].append(node)
        if stack:
            n = stack.pop()
            for next_node in edges[n]:
                if next_node not in visited:
                    stack.append(next_node)
                    DFS(next_node)
    DFS(V)
    # while stack:
    #     node = stack.pop()
    #     if node not in visited:
    #         answer[0].append(node)
    #     visited.append(node)
    #     for next_node in edges[node]:
    #         if next_node not in visited:
    #             stack.append(next_node)
    queue = []
    visited.clear()
    queue.append(V)
    while queue:
        node = queue.pop(0)
        visited.append(node)
        answer[1].append(node)
        for next_node in edges[node]:
            if next_node not in visited:
                visited.append(next_node)
                queue.append(next_node)
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    N,M,V = map(int,input().split())
    in_edge = [list(map(int,input().split())) for _ in range(M)]
    answer = my(N,M,V,in_edge)
    print(answer)
