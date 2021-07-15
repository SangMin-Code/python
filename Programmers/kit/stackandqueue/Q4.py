# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q4')


def my(prices:List[int])->List[int]:
    prices = [[i,j] for i,j in enumerate(prices)]
    stack =[]
    answer = [len(prices)-x-1 for x in range(len(prices))]

    for i,j in prices:
        while stack and j<stack[-1][1]:
            p = stack.pop()
            answer[p[0]]=i-p[0]
        stack.append([i,j])
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    prices = list(map(int,input().split()))
    answer = my(prices)
    print(answer)
