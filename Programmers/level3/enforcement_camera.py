#enforcement_camera.py
#https://programmers.co.kr/learn/courses/30/lessons/42884
import sys
sys.stdin=open('input/enforcement_camera')
from typing import List

def my(routes:List[List[int]])->int:
    answer = 1
    routes.sort(key=lambda x:x[0])
    c_start,c_end = routes[0]
    for route in routes[1:]:
        if route[0]<=c_end:
            c_start ,c_end = route[0], min(route[1],c_end)
        else:
            answer+=1
            c_start, c_end = route[0], route[1]
    return answer







TC = int(input())
for test_case in range(1,TC+1):
    n= int(input())
    routes = []
    for _ in range(n):
        routes.append(list(map(int,input().split())))
    answer = my(routes)
    print(answer)