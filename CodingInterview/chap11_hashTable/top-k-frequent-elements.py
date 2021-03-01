#top-k-frequent-elements

import sys
from typing import List
import collections
sys.stdin=open('input/top-k-frequent-elements')
import heapq

def my(nums:List[int],k:int)->List:
    k_list = collections.Counter(nums)
    sort_list = k_list.most_common()
    answer = []
    for i in range(k):
        answer.append(sort_list[i][0])
    return answer

def using_heap(nums:List[int],k:int)->List[int]:
    freqs = collections.Counter(nums)
    freqs_heap = []
    #힙에 음수로 삽입
    for f in freqs:
        heapq.heappush(freqs_heap,(-freqs[f],f))
    topk = list()
    #k번 만큼 추출, 최소합(Min Heap) 이므로 가장 작은 음수 순으로 추출
    for _ in range(k):
        topk.append(heapq.heappop(freqs_heap)[1])
    return topk

def pyhthonic(nums:List[int], k:int)->List:
    return list(zip(*collections.Counter(nums).most_common()))[0]

k = int(input())
nums = list(map(int,input().split()))

print(my(nums,k))
print(using_heap(nums,k))