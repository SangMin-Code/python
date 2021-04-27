#dijkstra 알고리즘
'''
다익스트라 알고리즘.
-> 하나의 시작 정점으로부터 다른 모든 정점까지의
   최단경로를 찾는 알고리즘
원리
graph 자료구조를 사용ㅎ아여 노드와 가중치를 가진 간선을 이용하여
실제 거리를 표현.
1. 출발 노드와, 도착노드를 설정
2. 주어진 모든 거리 값을 부여
3. 출발 노드부터 시작하여 방문하지 않았던 노드를 방문하고 거리를 계산한 다음
   현재 알고있는 거리보다 짧으면 해당 값으로 갱신
4. 현재 노드에 인접한 모든 미방문 노드까지의 거리를 계산했다면 현재 노드는
   방문한 것이므로 미방문 집합에서 제거
5. 도착 노드가 미방문 노드 집합에서 벗어나면 알고리즘 종료

* 방문하지 않은 인접 노드를 방문할때 우선순위 큐를 사용하면 지금까지
  발견된 가장 짧은 거리의 노드에 대해서 먼저 계산할 수 있고
   더 긴 거리로 계산되었을 시 스킵
'''
import collections
from typing import List
import sys
import heapq
sys.stdin=open('input/dijkstra')
n = int(input())
input_list  = [list(map(int,i.split()))for i in list(input().split(','))]
graph = collections.defaultdict(list)
for s,e,v in input_list:
    graph[s].append([e,v])
    graph[e].append([s,v])


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