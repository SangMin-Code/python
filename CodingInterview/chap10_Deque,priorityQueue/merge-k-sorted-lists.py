#merge-k-sorted-lists
'''
3
1 4 5
1 3 4
2 6
'''

import sys
from typing import List
sys.stdin = open('input/merge-k-sorted-lists')
import heapq


class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None

def my(nodes:List[ListNode])->ListNode:
    answer = ListNode(None)
    head = answer
    while nodes:
        min = sys.maxsize
        idx = 0
        t = ListNode(None)
        for i, node in enumerate(nodes) :
            if min>node.value:
                idx = i
                t = node
                min = node.value
        head.next = t
        head = head.next
        nodes[idx]=nodes[idx].next
        if nodes[idx]==None:
            nodes.pop(idx)
    return answer.next

def mergeKLists(lists:List[ListNode])->ListNode:
    root = result = ListNode(None)
    heap = []

    #각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap,(lists[i].val,i,lists[i]))
    #힙 추출 이후 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[i]
        result.next=node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap,(result.next.val,idx,result.next))
    return root.next

TC = int(input())
nodeList = [ListNode(None) for i in range(TC)]
for i in range (TC):
    t = list(map(int,input().split()))
    node =nodeList[i]
    for j in t :
        node.next = ListNode(j)
        node = node.next
    nodeList[i]=nodeList[i].next

answer =my(nodeList)

while answer :
    print(answer.value)
    answer = answer.next