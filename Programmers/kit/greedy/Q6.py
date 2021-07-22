# Q6.py
import sys
from typing import List

sys.stdin = open('input/Q6')


def my(routes:List[List[int]])->int:
    answer =1
    routes.sort(key=lambda x:x[0])
    c_start,c_end = routes[0],routes[1]
    for route in routes[1:]:
        if route[0]<=c_end:
            c_start,c_end = routes[0],min(route[1],c_end)
        else:
            answer+=1
            c_start,c_end = routes[0],route[1]
    return answer

def my(routes:List[List[int]])->int:
    answer =1
    routes.sort(key=lambda x:x[0])
    c_s,c_e = routes[0],routes[1]
    for route in routes[1:]:
        if route[0]<=c_e:
            c_s,c_e = routes[0],min(route[1],c_e)
        else:
            answer+=1
            c_s,c_e = routes[0],route[1]
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    routes = [list(map(int,i.split())) for i in input().split(',')]
    answer = my(routes)
    print(answer)
