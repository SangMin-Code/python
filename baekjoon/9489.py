# 9489.py
import sys
from typing import List

sys.stdin = open('input/9489')
import collections

def my(n:int, k:int, nodes:List[int])->int:
    answer = []
    queue = collections.deque()
    queue.append([nodes[0],0,-1])

    parent = 0
    level = 0

    a_p,a_l = 0,0
    for i in range(1,n):
        if i==1 or nodes[i-1]+1 != nodes[i]:
            node = queue.popleft()
            level = node[1] + 1
            parent = node[0]

        queue.append([nodes[i],level,parent])
        answer.append([nodes[i],level,parent])

        if nodes[i]==k:
            a_p,a_l = parent,level

    result =0
    for i in answer:
        if i[1]==a_l and i[2]!=a_p:
            result+=1

    return result

# def my(n:int, k:int, nodes:List[int])->int:
#     p =[-1]*n
#     cnt = -1
#     idx = 0
#     for i in range(1,n):
#         if nodes[i]==k:
#             idx = i
#         if nodes[i]!=nodes[i-1]+1:
#             cnt+=1
#         p[i]=cnt
#     answer = 0
#     for i in range(1,n):
#         if p[i]!=p[idx] and p[p[i]]==p[p[idx]]:
#             answer+=1
#     return answer


# TC = int(input())
# for test_case in range(1, TC + 1):
#     n,k = map(int,sys.stdin.readline().rstrip().split())
#     nodes = list(map(int,sys.stdin.readline().rstrip().split()))
#     answer = my(n,k,nodes)
#     print(answer)

while True:
    n,k = map(int,sys.stdin.readline().rstrip().split())
    if n==0 and k==0:
        break
    nodes = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(n,k,nodes)
    print(answer)