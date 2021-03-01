import sys
import collections
sys.stdin = open('input/minimum_height_trees')
from typing import List

def my(n:int,edges:List[List[int]]):
    dic = collections.defaultdict(list)
    cnt = collections.defaultdict(int)
    for i,j in edges:
        dic[i].append(j)
    #TODO minumum-heigh-trees

def findMinHeightTrees(n:int, edges:List[List[int]])->List[int]:
    if n <=1 :
        return [0]
    graph = collections.defaultdict(list)
    for i, j in edges :
        graph[i].append(j)
        graph[j].append(i)
    leaves = []
    for i in range(n+1):
        if len(graph[i])==1:
            leaves.append(i)
    while n >2:
        n-=len(leaves)
        new_leaves =[]
        for leaf in leaves:
            neighbor = graph[leaf].pop()
            graph[neighbor].remove(leaf)
            if len(graph[neighbor])==1:
                new_leaves.append(neighbor)
        leaves=new_leaves
    return leaves



dic = collections.defaultdict(list)

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    num = int(input())
    edges =[]
    for i in range(num):
        edges.append(list(map(int,input().split())))
    my(n,edges)
