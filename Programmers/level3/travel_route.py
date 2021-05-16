#travel_route.py
import sys
sys.stdin=open('input/travel_route')
from typing import List
import collections
import copy
def my(tickets:List[List[str]])->List[str]:
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    route, stack = [], ['ICN']
    while stack:
        # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    return route[::-1]

def test(tickets:List[List[str]])->List[str]:
    val = []
    graph = collections.defaultdict(list)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
    route = ['ICN']
    def DFS(s,in_graph):
        if len(route)==len(tickets)+1:
            val.append(route[:])
        elif len(route)<len(tickets)+1 and not val:
            for i in in_graph[s]:
                next_graph = copy.deepcopy(in_graph)
                route.append(i)
                next_graph[s].remove(i)
                DFS(i,next_graph)
                route.pop()
    DFS('ICN',graph)
    return val[0]

def my2(tickets:List[List[str]])->List[str]:
    answer = []
    dic = collections.defaultdict(list)
    for a,b in sorted(tickets):
        dic[a].append(b)
    route=['ICN']
    def DFS(s,in_dic):
        if len(route)==len(tickets)+1:
            answer.append(route[:])
        elif len(route)<len(tickets)+1:
            for i in in_dic[s]:
                next_dic = copy.deepcopy(in_dic)
                route.append(i)
                next_dic[s].remove(i)
                DFS(i,next_dic)
                route.pop()
    DFS('ICN',dic)
    return answer[0]

def my3(tickets:List[List[str]])->List[str]:
    answer = []
    dic = collections.defaultdict(list)
    for a, b in sorted(tickets):
        dic[a].append(b)
    route = ['ICN']
    def DFS(s):
        if len(route) == len(tickets)+ 1:
            answer.append(route[:])
        elif len(route) < len(tickets)+1:
            for i in dic[s]:
                route.append(i)
                dic[s].remove(i)
                DFS(i)
                route.pop()
    DFS('ICN')
    return answer[0]

TC = int(input())
for test_case in range(1,TC+1):
    tickets =[]
    temp = list(input().split(','))
    for i in temp:
        s,e = i.split()
        tickets.append([s,e])
    #answer = my(tickets)
    answer = my3(tickets)
    print(answer)