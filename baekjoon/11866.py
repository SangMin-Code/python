# 11866.py
# queue 큐
import collections
import sys
from typing import List

sys.stdin = open('input/11866')


def my(N:int,K:int)->List[str]:
    answer = []
    queue = collections.deque([i+1 for i in range(N)])

    while queue:
        for _ in range(K-1):
            queue.append(queue.popleft())
        answer.append(str(queue.popleft()))

    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    N,K = map(int,sys.stdin.readline().rstrip().split())
    answer = my(N,K)
    print('<'+', '.join(answer)+'>')
