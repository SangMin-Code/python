import sys
sys.stdin =open('input/reconstruct-itinerary')
import collections
from typing import List

TC = int(input())

def my(dic:dict)->List[str]:
    result = []
    def dfs(str_from:str):
        result.append(str_from)
        list = dic[str_from]
        if not list:
            return
        str_to =list[0]
        #list.pop(0)
        #dic[str_from]=list
        list.remove(str_to)
        dic[str_from]=list
        #TODO method 실행순서??
        #python 내부 method 실행순서??? -> dic[str_from]=list.remove(str_to) 오류
        dfs(str_to)
    dfs("JFK")
    return result
def find_itinerary(tickets:List[List[str]])->List[str]:
    graph = collections.defaultdict(list)
    for a,b in sorted(tickets,reverse=True):
        graph[a].append(b)
    route = []
    def dfs(a):
        while graph[a]:
            dfs(graph[a].pop())
        route.append(a)
    dfs('JFK')
    return route[::-1]
def using_stack(tickets:List[List[str]])->List[str]:
    graph = collections.defaultdict(list)
    #그래프 순서대로 구성
    for a,b in sorted(tickets):
        graph[a].append(b)
    route, stack = [],['JFK']
    while stack:
        #반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())
    return route[::-1]
for i in range(1,TC+1):
    n = int(input())
    dic = collections.defaultdict(list)
    strs = []
    for j in range(n):
        temp = list(input().split())
        strs.append(temp)
        dic[temp[0]].append(temp[1])
        dic[temp[0]]=sorted(dic[temp[0]])
    #print(my(dic))
    #print(find_itinerary(strs))
    print(using_stack(strs))