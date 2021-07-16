# Q1.py
import heapq
import sys
from typing import List

sys.stdin = open('input/Q3')

def my(operations:List[str])->List[int]:
    answer = [0,0]
    heap = []
    for i in operations:
        if i == 'D 1' and heap:
            heap.pop()
        elif i =='D -1' and heap:
            heapq.heappop(heap)
        elif 'I' in i:
            t,num = i.split()
            heapq.heappush(heap,int(num))
        if heap:
            answer = [heap[-1],heap[0]]
        return answer

def my2(operations:List[str])->List[int]:
    max_heap=[]
    min_heap=[]

    for i in operations:
        if i == 'D 1':
            if max_heap:
                heapq.heappop(max_heap)
                if not max_heap or -max_heap[0]<min_heap[0]:
                    max_heap,min_heap=[],[]
        elif i =='D -1':
            if min_heap:
                heapq.heappop(min_heap)
                if not min_heap or -max_heap[0]<min_heap[0]:
                    max_heap,min_heap=[],[]
        else:
            a,num = map(int,i.split())
            heapq.heappush(max_heap,-num)
            heapq.heappush(min_heap,num)
    if not min_heap:
        return [0,0]
    return [-heapq.heappop(max_heap),heapq.heappop(min_heap)]


TC = int(input())
for test_case in range(1, TC + 1):
    operations  = list(input().split(','))
    answer = my(operations)
    print(answer)
