# make_all_zeros.py
import sys
from typing import List
import collections
sys.stdin = open('input/make_all_zeros')

'''
#시간초과 걸림
def my(a:List[int], edges:[List[List[int]]])->int:
    answer = 0
    if sum(a)!=0:
        return -1
    dic = collections.defaultdict(list)
    for n1,n2 in edges:
        dic[n1].append(n2)
        dic[n2].append(n1)
    queue = collections.deque()
    for i in dic:
        if len(dic[i])==1:
            queue.append(i)
    while queue:
        node = queue.popleft()
        for next_node in dic[node]:
            answer+=abs(a[node])
            a[next_node]+=a[node]
            a[node]=0
            dic[next_node].remove(node)
            if len(dic[next_node])==1:
                queue.append(next_node)
    return answer
'''
def my(a:List[int], edges:[List[List[int]]])->int:
    if sum(a) != 0:
        return -1
    graph = collections.defaultdict(list)
    for u,v in edges:
        graph[u].append(v)
        graph[v].append(u)
    def dfs(c,p):
        cnt = 0
        for next_node in graph[c]:
            if next_node != p:
                cnt+=dfs(next_node,c)
        cnt += abs(a[c])
        a[p]+=a[c]
        a[c]=0
        return cnt
    return dfs(0,0)

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
'''
TC = int(input())
for test_case in range(1, TC+1):
    a = list(map(int,input().split()))
    edges = [list(map(int,i.split())) for i in list(input().split(','))]
    print(my(a,edges))