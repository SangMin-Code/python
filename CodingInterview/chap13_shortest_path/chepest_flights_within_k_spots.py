#chepest_flights_within_k_spots

import sys
sys.stdin = open('input/chepest_flights_within_k_spots')
from typing import List
import collections
import heapq

def my (n:int, flights:List[List[int]], src:int, dst:int, K:int)->int:
    graph = collections.defaultdict(list)
    for u,v,w in flights:
        graph[u].append((v,w))
    Q = [(0,src,K)]
    while Q:
        price, node, k =heapq.heappop(Q)
        if node == dst :
            return price
        if k>=0:
            for v,w in graph[node]:
                alt = price+w
                heapq.heappush(Q,(alt,v,k-1))
    return -1

def find_chepesrs_price(n:int, flights:List[List[int]], src:int, dst:int, K:int)->int:
    graph = collections.defaultdict(list)
    for u,v,w in flights:
        graph[u].append((v,w))
    #큐 변수 :[(가격, 정점, 남은 가능 경유지 수 )]
    Q = [(0,src,K)]
    #우선순위 큐 최솟값 기준으로 도착점까지 최소 비용 파별
    while Q :
        price, node, k = heapq.heappop(Q)
        if node == dst:
            return price
        if k>=0:
            for v,w in graph[node]:
                alt = price+w
                heapq.heappush(Q,(alt,v,k-1))
    return -1



n = int(input())
src = int(input())
dst = int(input())
K = int(input())
edges = []
for _ in range(n):
    edges.append(list(map(int,input().split())))

result =find_chepesrs_price(n,edges,src,dst,K)
print(result)