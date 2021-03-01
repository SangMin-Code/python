#network-delay-time
import sys
from operator import ne

sys.stdin = open('input/network-delay-time')
from typing import List
import collections
import heapq

#TODO heapq 이용하여 최단경로 탐색

class edge():
    def __init__(self,goal,time):
        self.goal=goal
        self.time=time
def my(N:int,K:int,e:List[List[int]]):
    graph = collections.defaultdict(list)
    for u,v,w in e:
        graph[u].append((v,w))
    dist = collections.defaultdict(int)
    Q = [(0,K)] #distance, K
    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node]=time
            for v,w in graph[node]:
                alt = time+w
                heapq.heappush(Q,(alt,v))
    if len(dist)==N:
        return max(dist.values())
    return -1

def networkDelayTime(times:List[List[int]], N:int, K:int)->int:
    graph = collections.defaultdict(list)
    #그래프 인접 리스트 구성
    for u,v,w in times:
        graph[u].append((v,w))
    #큐 변수: [(소요 시간, 정점)]
    Q=[(0,K)]
    dist = collections.defaultdict(int)
    #우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while Q:
        time, node = heapq.heappop(Q)
        #time, node = Q.pop(0)
        if node not in dist:
            dist[node] = time
            for v,w in graph[node]:
                alt = time+w
                heapq.heappush(Q,(alt,v))
                #Q.append((alt,v))
    #모든 노드의 최단 경로 존재 여부 판별
    if len(dist)==N:
        return max(dist.values())
    return -1



N = int(input())
K = int(input())
enum = int(input())
e=[]
for i in range(enum):
    e.append(list(map(int,input().split())))
#print(my(N,K,e))
val = networkDelayTime(e,N,K)
print(f'val:{val}')