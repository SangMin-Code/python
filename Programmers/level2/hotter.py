
#https://programmers.co.kr/learn/courses/30/lessons/42626
#heap/더 맵게게

import sys
sys.stdin = open('input/hotter')
import heapq
from typing import List


def my(k:int, foods:List[int])->int:
    heap = []
    for i in foods:
        heapq.heappush(heap,i)
    result = 0
    while heap[0]<k:
        food1 = heapq.heappop(heap)
        food2 = heapq.heappop(heap)
        heapq.heappush(heap,food1+food2*2)
        result+=1
    if heap[0]<k and len(heap)<2:
        return -1
    return result

def practice(k:int, scoville:List[int])-> int:
    heapq.heapify(scoville)  #heapq 사용
    answer =0
    while scoville[0]<k and len(scoville)>1:  #pop을 두개씩 해야하므로 1개만 남았을때는 뒤에서 확인
        food1 = heapq.heappop(scoville)
        food2 = heapq.heappop(scoville)
        heapq.heappush(scoville,food1+food2*2)
        answer+=1
    if scoville[0]<k:  # 더 이상 섞을 수 없는 경우
        return -1
    return answer


k = int(input())
foods = list(map(int,input().split()))
print(my(k,foods))

