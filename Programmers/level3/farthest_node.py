#farthest_node.py
import sys
sys.stdin=open('input/farthest_node')
from typing import List
import collections

def my(n:int, vertex:List[int])->int:
    answer = 0
    distance = [0 for i in range(n+1)]
    distance[1]=1
    queue = collections.deque()
    nodes = collections.defaultdict(list)
    for n1,n2 in vertex:
        nodes[n1].append(n2)
        nodes[n2].append(n1)

    queue.append(1)

    while queue:
        node = queue.popleft()
        for i in nodes[node]:
            if distance[i]==0:
                distance[i] = distance[node] + 1
                queue.append(i)
    max_val = max(distance)

    for i in distance:
        if i == max_val:
            answer+=1
    return answer


TC = int(input())
for test_case in range(1,TC+1):
    n,m = map(int,input().split())
    vertex = [ ]
    for _ in range(m):
        vertex.append(list(map(int,input().split())))
    answer = my(n,vertex)
    print(answer)