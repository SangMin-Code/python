#sw5102.py

import sys
from math import pi

sys.stdin = open("/input/sample_input.txt", "r")

def find(start):
    queue.append(start)
    global  result
    visited[start]=True
    while queue :
        x=queue.pop(0)
        for i in cList[x]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                distance[i] = distance[x]+1
                if i == goal :
                    result = distance[i]
'''
def find(start):
    global  result
    visited[start]=True
    x = queue.pop(0)
    for i in cList[x]:
        if not visited[i]:
            queue.append(i)
            distance[i] = distance[x] + 1
            find(i)
            if i == goal:
                result = distance[i]
                return
'''
TC = int(input())
for test_case in range(1,TC+1):
    #v: 노드 수 , e:간선 수
    v,e = map(int, input().split())
    cList =[[] for i in range(v+1)]
    for i in range(e):
        a,b = map(int, input().split())
        if b not in cList[a]:
            cList[a].append(b)
        if a not in cList[b]:
            cList[b].append(a)
    start,goal=map(int,input().split())
    result = 0
    distance =[0 for i in range(v+1)]
    visited = [ False for i in range(v+1)]
    queue =[]
    #queue.append(start)
    find(start)
    print(f'#{test_case} {result}')
