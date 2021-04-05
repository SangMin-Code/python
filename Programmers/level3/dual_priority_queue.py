#dual_priority_queue.py
import sys
sys.stdin=open('input/dual_priority_queue')
from typing import List
import heapq

def my(operations:List[str])->List[int]:
    answer = [0,0]
    heap=[]
    for i in operations:
        if i == 'D 1' and heap:
            heap.pop()
        elif i == 'D -1' and heap:
            heapq.heappop(heap)
        elif 'I' in i:
            t,num = i.split()
            heapq.heappush(heap, int(num))
    if heap:
        answer = [max(heap), min(heap)]
    return answer


TC = int(input())
for test_case in range(1,TC+1):
    operations = list(input().split(','))
    answer =my(operations)
    print(answer)
