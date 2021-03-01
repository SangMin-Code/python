#sw5099.py

import sys
from math import pi

sys.stdin = open("/input/sample_input.txt", "r")

TC = int(input())

for test_case in range(1, TC+1):
    #N:화덕 가용량, M 피자 수
    N,M = map(int,input().split())
    pizzaList = list(map(int,input().split()))
    pList = []
    for i in range(M):
        pList.append([pizzaList[i],i+1])
    queue = []
    result = 0
    for i in range(N):
        queue.append(pList[i])
        pList.pop(0)

    while(queue):
        if queue[0][0]//2 != 0:
            t = queue.pop(0)
            t[0]=t[0]//2
            queue.append(t)
        else:
            result =queue.pop(0)[1]
            if len(pList) != 0:
                queue.append(pList.pop(0))
    print(f'#{test_case} {result}')
