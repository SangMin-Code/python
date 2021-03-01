#DFS_BFS.py



#DFS reculsive
from typing import re


def reculsiveDFS(v,discovered=[]):
    discovered.append(v)
    for w in graph[v]:
        if w not in discovered:
            discovered = reculsiveDFS(w,discovered)
    return discovered

def iterativeDFS(start_v):
    discovered =[]
    stack=[start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered

def iterative_BFS(start_v):
    '''
    discovered = []
    queue = [start_v]
    while queue:
        v=queue.pop(0)
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                queue.append(w)
    return discovered
    '''
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered


graph = {
    1:[2,3,4],
    2:[5],
    3:[5],
    4:[],
    5:[6,7],
    6:[],
    7:[3]
}

print(reculsiveDFS(1))
print(iterativeDFS(1))
print(iterative_BFS(1))