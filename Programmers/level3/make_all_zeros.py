# make_all_zeros.py
import sys
from typing import List
import collections
sys.stdin = open('input/make_all_zeros')
'''
def my(a:List[int], edges:[List[List[int]]])->int:
    answer = 0
    if sum(a)!=0:
        return -1
    dic = collections.defaultdict(list)
    for n1,n2 in edges:
        dic[n1].append(n2)
        dic[n2].append(n1)
    stack =[[0,0]]
    while stack:
        print(stack)
        node, prev_node = stack.pop()
        if not dic[node]:
            answer +=abs(a[node])
            a[prev_node]+=a[node]
            a[node]=0
        else :
            next_nodes = dic[node]
            for next_node in next_nodes:
                dic[next_node].remove(node)
                stack.append([next_node,node])
    if sum(a)==0:
        return answer+abs(a[0])
    else :
        return -1
'''

def my(a, edges):
    answer = []
    if sum(a) != 0:
        return -1
    graph = collections.defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def dfs(child, parent):
        for node in graph[child]:
            if node != parent:
                dfs(node,child)
        answer.append(abs(a[child]))
        a[parent] += a[child]
        a[child] = 0
    dfs(0,0)
    return sum(answer)

TC = int(input())
for test_case in range(1, TC+1):
    a = list(map(int,input().split()))
    edges = [list(map(int,i.split())) for i in list(input().split(','))]
    print(my(a,edges))