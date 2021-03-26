#network.py
#https://programmers.co.kr/learn/courses/30/lessons/43162
import sys
sys.stdin=open('input/network')
from typing import List

def my(n:int, computers:List[int])->int:
    com = [[] for _ in range(n)]
    for i,net in enumerate(computers):
        for j in range(n):
            if net[j]==1 and j not in com[i] and j!=i:
                com[i].append(j)
    can = [False for i in range(n)]
    def DFS(node):
        for i in com[node]:
            if can[i]==False:
                can[i]=True
                DFS(i)
    cnt=0
    for i in range(n):
        if can[i]==False:
            cnt+=1
        DFS(i)
    return cnt



TC = int(input())
for test_case in range(1,TC+1):
    n,t = map(int,input().split())
    computers =[]
    for _ in range(t):
        computers.append(list(map(int,input().split())))
    answer = my(n,computers)
    print(answer)