import sys
sys.stdin = open('input/course_schedule')
from typing import List
import collections


#TODO DFS 순환구조 판별
def can_finish(numCoureses:int, prerequisites:List[List[int]])->bool:
    graph = collections.defaultdict(list)
    for x,y in prerequisites:
        graph[x].append(y)
    traced = set()
    visited = set()
    def dfs(i):
        if i in traced:
            return False
        if i in visited:
            return True
        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False
        traced.remove(i)
        visited.add(i)
        return True
    for x in list(graph):
        if not dfs(x):
            return False
    return True

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    N = int(input())
    course = []
    for i in range(N):
        course.append(list(map(int,input().split())))
    print(can_finish(n,course))
