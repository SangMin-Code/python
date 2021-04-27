# sharing_taxi.py
import collections
import heapq
import sys
from typing import List

sys.stdin = open('input/sharing_taxi')

def my(n:int, s:int, a:int, b:int, fares:List[List[int]])->int:
    graph = collections.defaultdict(list)
    for n1,n2,cost in fares:
        graph[n1].append([n2,cost])
        graph[n2].append([n1,cost])

    def dijkstra(start,end,n):
        table = [float('inf')]*(n+1)
        table[start]=0
        queue = [[0,start]]

        while queue:
            val, node = heapq.heappop(queue)
            if table[node] < val: continue
            for new_node, new_cost in graph[node]:
                new_cost+=val
                if new_cost < table[new_node]:
                    table[new_node]=new_cost
                    heapq.heappush(queue,[new_cost,new_node])
        return table[end]

    cost = float('inf')
    for i in range(1, n + 1):
        cost = min(cost, dijkstra(s, i,n) + dijkstra(i, a,n) + dijkstra(i, b,n))
    return cost

TC = int(input())
for test_case in range(1, TC + 1):
    n,s,a,b = map(int,input().split())
    fares = [list(map(int,i.split()))for i in list(input().split(','))]
    answer = my2(n,s,a,b,fares)
    print(answer)
