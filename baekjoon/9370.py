# 9370.py
import collections
import heapq
import sys
from typing import List

sys.stdin = open('input/9370')


def my(n:int,s:int,g:int,h:int,edges:List[List[int]],goals:List[int])->List[int]:
    dic = collections.defaultdict(list)
    for n1,n2,v in edges:
        if (n1==g and n2==h) or (n1==h and n2==g):
            dic[n1].append([n2,v-0.1])
            dic[n2].append([n1,v-0.1])
        else:
            dic[n1].append([n2,v])
            dic[n2].append([n1,v])

    def dijkstra(start,n,goals):
        visited = [float('inf')]*(n+1)
        visited[start]=0
        heap =[]
        heapq.heappush(heap,[0,start])
        while heap:
            value,now = heapq.heappop(heap)
            if visited[now]<value:
                continue
            for next_node,next_val in dic[now]:
                new_val = next_val+value
                if new_val < visited[next_node]:
                    visited[next_node]=new_val
                    heapq.heappush(heap,[new_val,next_node])
        answer = []
        for i in goals:
            if visited[i] != float('inf') and not float(visited[i]).is_integer():
                answer.append(i)
        return sorted(answer)
    return list(map(int, dijkstra(s,n,goals)))


TC = int(input())
for test_case in range(1, TC + 1):
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(m)]
    goals =[int(input()) for _ in range(t)]
    answer = my(n,s,g,h,edges,goals)
    print(' '.join(list(map(str,answer))))

