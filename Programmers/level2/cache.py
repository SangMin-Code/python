#cache.py
#https://programmers.co.kr/learn/courses/30/lessons/17680
import sys
sys.stdin=open('input/cache')
from typing import List
import collections

def my(cacheSize:int, cities:List[str])->int:
    for i,s in enumerate(cities):
        cities[i]=s.lower()
    queue = collections.deque()
    if cacheSize==0:
        return len(cities)*5
    time = 0
    for city in cities:
        if city in queue:
            queue.remove(city)
            queue.append(city)
            time+=1
        else :
            if len(queue)==cacheSize:
                queue.popleft()
            queue.append(city)
            time+=5
    return time

TC = int(input())
for test_case in range(1,TC+1):
    cacheSie = int(input())
    cities = list(input().lower().split())
    answer = my(cacheSie,cities)
    print(answer)