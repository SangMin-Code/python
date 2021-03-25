#delivery.py
import sys
import collections
sys.stdin=open('input/delivery')
from typing import List

def my(N:int,K:int,road:List[List[int]])->int:
    queue = collections.deque()
    dic = collections.defaultdict(list)
    temp = [[500001]*(N+1) for i in range(N+1)]
    for node1, node2, val in road:
        temp[node1][node2] = min(val,temp[node1][node2])
        temp[node2][node1] = min(val, temp[node2][node1])
        #dic[node1].append([node2, val])
        #dic[node2].append([node1, val])
    #road중 최소만 남기기
    for i in range(1,N+1):
        for j in range(1,N+1):
            if temp[i][j]!=500001:
                dic[i].append([j,temp[i][j]])
    nodes = set()
    nodes.add(1)
    queue.append([1, K, 0])
    while queue:
        node, d, prev_node = queue.popleft()
        for next_node, val in dic[node]:
            if d - val >= 0 and next_node != prev_node:
                nodes.add(next_node)
                queue.append([next_node, d - val, node])
    return len(nodes)

TC = int(input())
for test_case in range(1,TC+1):
    N,K,n = map(int,input().split())
    road = []
    for _ in range(n):
        road.append(list(map(int,input().split())))
    answer = my(N,K,road)
    print(answer)


    '''
    visited = [False] * (N + 1)
    dists = [inf] * (N + 1)
    dists[1] = 0
    q = deque([1])

    while q:
        parent = q.popleft()
        visited[parent] = True

        for node1, node2, dist in road:
            if node1 == parent or node2 == parent:
                target = node1
 
                if node1 == parent:
                    target = node2

                if dists[target] > dists[parent] + dist:
                    dists[target] = dists[parent] + dist
                    q.append(target)

    return sum(1 for d in dists if d <= K)
    '''