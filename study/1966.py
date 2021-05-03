# 1966.py
# queue 큐
import sys
from typing import List

sys.stdin = open('input/1966')
import collections

def my(N:int, M:int, documents:List[int])->int:
    val_queue = []
    print_queue = collections.deque()
    for i,v in enumerate(documents):
        val_queue.append(v)
        print_queue.append([i,v])
    val_queue=collections.deque(sorted(val_queue,reverse=True))
    cnt = 0
    while print_queue:
        d = print_queue.popleft()
        if d[1]==val_queue[0]:
            val_queue.popleft()
            cnt+=1
            if d[0]==M:
                break
        else :
            print_queue.append(d)
    return cnt

TC = int(input())
for test_case in range(1, TC + 1):
    N,M = map(int,sys.stdin.readline().rstrip().split())
    documents = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(N,M,documents)
    print(answer)
