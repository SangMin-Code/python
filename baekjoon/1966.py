# 1966.py
# queue 큐
import sys
from typing import List

sys.stdin = open('input/1966')
import collections

def my(N:int, M:int, documents:List[int])->int:
    #프린터에 대기하고있는 현재 문서 이상 중요 문서가 없는것을 확인해야 함
    #->대기 문서의 중요도를 내림차순으로 정렬하여 현재 문서의 중요도와 정렬문서의 맨 앞 원소와 비교
    # 중요도가 동일할 경우 중요도 목록을 popleft 하여 현재 문서보다 중요도가 높은 문서가 있는지의 문제를 해결 
    # 매번 자신보다 중요도가 높은 문서를 검색하면 시간초과 문제 생길듯
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
