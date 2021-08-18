# Q4.py.py
import sys
from typing import List
import collections

sys.stdin = open('input/Q4')


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


TC = int(input())
for test_case in range(1, TC + 1):
    tickets = [list(i.split()) for i in input().split(',')]
    answer = my(tickets)
    print(answer)
