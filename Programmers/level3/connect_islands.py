#connect_islands.py
#https://programmers.co.kr/learn/courses/30/lessons/42861
import sys
sys.stdin=open('input/connect_islands')
from typing import List

def my(n:int,costs:List[int])->int:
    answer = 0
    costs.sort(key = lambda x: x[2])
    connection = [costs[0][0]]
    while len(connection) != n:
        for i, cost in enumerate(costs):
            if (cost[0] in connection) and (cost[1] in connection): continue
            if (cost[0] in connection) or (cost[1] in connection):
                answer += cost[2]
                connection.append(cost[0])
                connection.append(cost[1])
                connection = list(set(connection))
                costs.pop(i)
                break
    return answer

TC = int(input())
for test_case in range(1,TC+1):
    n,m = map(int,input().split())
    costs = []
    for _ in range(m):
        costs.append(list(map(int,input().split())))
    answer = my(n,costs)
    print(answer)