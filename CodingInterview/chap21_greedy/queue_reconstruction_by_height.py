import sys
sys.stdin = open('input/queue_reconstruction_by_height')
from typing import List
import heapq

def reconstructQueue(people:List[List[int]])->List[List[int]]:
    heap = []
    for person in people:
        heapq.heappush(heap,[-person[0],person[1]])
    result = []
    while heap:
        person = heapq.heappop(heap)
        result.insert(person[1],[-person[0],person[1]])
    return result



n = int(input())
heights = []
for _ in range(n):
    temp = list(map(int,input().split()))
    heights.append(temp)
answer =reconstructQueue(heights)
print(answer)
