# 15649.py
import sys
from typing import List

sys.stdin = open('input/15649')


def my(N:int,M:int)->List[List[int]]:
    nums = [i for i in range(1,N+1)]
    answer = []
    stack = []

    def dfs(n,list):
        stack.append(n)

        if len(stack)==M:
            answer.append(stack[:])
            stack.pop()
            return

        next_list = list[:]
        next_list.remove(n)

        for i in next_list:
            dfs(i,next_list)

        stack.pop()

    for i in nums:
        dfs(i,nums)

    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    N,M = map(int,input().split())
    answer = my(N,M)
    for i in answer:
        print(' '.join(map(str,i)))
