# Q5.py
import sys
from typing import List

sys.stdin = open('input/Q5')


def my(n:int,costs:List[List[int]])->int:
    answer = 0
    costs.sort(key=lambda x:x[2])
    connection =[costs[0][0]]

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
for test_case in range(1, TC + 1):
    n = int(input())
    costs = [list(map(int,i.split())) for i in input().split(',')]
    answer = my(n,costs)
    print(answer)
