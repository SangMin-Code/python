# 1753.py
import collections
import heapq
import sys
from typing import List

sys.stdin = open('input/1753')


def my(V:int,E:int,K:int,edges:List[List[int]])->List[str]:
    graph = collections.defaultdict(list)
    for s,e,v in edges:
        graph[s].append([e,v])
        #graph[e].append([s,v])
    def dijkstra(graph,start,n):
        distances = [float('inf') for _ in range(n+1)]
        distances[start]=0
        queue = []
        heapq.heappush(queue,[distances[start],start])
        while queue:
            c_distance, c_destination = heapq.heappop(queue)
            if distances[c_destination]<c_distance:
                continue
            for new_destination,new_distance in graph[c_destination]:
                distance = c_distance+new_distance
                if distance < distances[new_destination]:
                    distances[new_destination] = distance
                    heapq.heappush(queue,[distance,new_destination])
        return distances
    return [ str(i).upper() for i in dijkstra(graph,K,V)]

TC = int(input())
for test_case in range(1, TC + 1):
    V,E = map(int,input().split())
    K = int(input())
    edges = [list(map(int,input().split())) for _ in range(E)]
    answer = my(V,E,K,edges)
    print(answer)


'''

def dijkstra(graph,start,n):
    distances = [float('inf') for _ in range(n+1)] #시작지점으로부터의 거리 값을 저장
    distances[start]=0 #시작지점에서는 가중치 0
    queue =[]
    heapq.heappush(queue,[distances[start],start]) #시작 노드부터 탐색 시작
    while queue:
        current_distance,current_destination = heapq.heappop(queue) #탐색할 노드와 현재 거리를 가져옴
        if distances[current_destination] < current_distance: #기존에 있는 거리보다 멀면 패스
            continue
        for new_destination, new_distance in graph[current_destination]:
            distance=current_distance+new_distance #해당 노드를 거치면서 거리 증가
            if distance < distances[new_destination]: # 해당 노드가 가진 거리보다 작으면 갱신
                distances[new_destination]=distance
                heapq.heappush(queue,[distance,new_destination]) # 다음 인접 거리를 계산하기 위해 큐에 삽입
    return distances

print(dijkstra(graph,1,n))
'''