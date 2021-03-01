from typing import List
import sys
sys.stdin = open('input/k_closest_point_to_origin')
import heapq

def my(points:List[List[int]],k:int):
    points =sorted(points,key=lambda x: x[0]**2+x[1]**2)
    return points[:k]

def k_closest(points:List[List[int]],K:int)->List[List[int]]:
    heap = []
    for (x,y) in points:
        dist = x**2 + y**2
        heapq.heappush(heap,(dist,x,y))
    result = []
    for _ in range(K):
        (dist,x,y)=heapq.heappop(heap)
        result.append((x,y))
    return result


TC = int(input())
for test_case in range(1,TC+1):
    k = int(input())
    num = int(input())
    points = []
    for _ in range(num):
        point = list(map(int,input().split()))
        points.append(point)
    answer = my(points,k)
    print(answer)