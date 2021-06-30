# 1504.py
import collections
import heapq
import sys
from typing import List

sys.stdin = open('input/1504')


def my(N:int,E:int,edges:List[List[int]],v1:int,v2:int):

    dic = collections.defaultdict(list)
    for s,e,v in edges:
        dic[s].append([e,v])
        dic[e].append([s,v])

    def dijkstra(start,end):
        distances = [float('inf')]*(N+1)
        queue = []
        heapq.heappush(queue,[start,0])

        while queue:
            c_node,c_distance = heapq.heappop(queue)
            if  distances[c_node] < c_distance:
                continue
            for next_node, next_distance in dic[c_node]:
                new_distance = next_distance+c_distance
                if new_distance < distances[next_node]:
                    distances[next_node] = new_distance
                    heapq.heappush(queue,[next_node,new_distance])
        return distances[end]

    result = -1
    if v1 != 1 and v2 !=N:
        result = min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N)
                 ,dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N))
    elif v1 == 1 and v2 !=N:
        result = dijkstra(1,v2)+dijkstra(v2,N)
    elif v1 !=1 and v2 ==N:
        result = dijkstra(1,v1)+dijkstra(v1,N)
    else :
        result = dijkstra(1,N)


    if result == float('inf'):
        return -1
    return result


TC = int(input())
for test_case in range(1, TC + 1):
    N,E = map(int,sys.stdin.readline().rstrip().split())
    edges = [list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(E)]
    v1,v2 = map(int,sys.stdin.readline().rstrip().split())

    answer = my(N,E,edges,v1,v2)
    print(answer)
