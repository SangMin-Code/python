import sys
sys.stdin = open('input/assign_cookies')
from typing import List
import heapq
import bisect

def my(childs:List[int], cookies:List[int])->int:
    result = 0
    heap =[]
    childs.sort()
    for i in cookies:
        heapq.heappush(heap,i)
    for i in childs:
        if not heap:
            break
        cookie = heapq.heappop(heap)
        if cookie >= i:
            result+=1
        else :
            while cookie < i and heap:
                cookie =heapq.heappop(heap)
            if cookie>=i:
                result+=1
    return result

def greedy(g:List[int], s:List[int])->int:
    g.sort()
    s.sort()
    child_i=cookie_j=0
    while child_i<len(g) and cookie_j<len(s):
        if s[cookie_j]>=g[child_i]:
            child_i+=1
        cookie_j+=1
    return child_i

def binary_search(g:List[int], s:List[int])->int:
    '''
    하나의 리스트를 순회하면서 다른 하나는 이진 검색으로 찾는다.
    찾아낸 인덱스가 현재 부여한 아이들보다 클 경우 더 줄 수 있다는 말이므로 줄 수 있는
    아이들의 수를 1명 더 늘린다.
    '''
    g.sort()
    s.sort()
    result = 0
    for i in s:
        index = bisect.bisect_right(g,i)
        if index>result:
            result+=1
    return result

TC = int(input())
for test_case in range(1,TC+1):
    childs = list(map(int,input().split()))
    cookies = list(map(int,input().split()))
    answer = my(childs,cookies)
    print(answer)

