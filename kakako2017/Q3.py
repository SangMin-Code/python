#Q3.py
import sys
sys.stdin=open('input/Q3')
from typing import List
import collections

def my(cacheSize:int, cities:List[str])->int:
    cache = collections.deque()
    time = 0
    if cacheSize ==0:
        return len(cities)*5
    for city in cities:
        if city.lower() not in cache:
            time+=5
        else :
            time+=1
        if len(cache)==cacheSize:
            cache.popleft()
        cache.append(city.lower())

    return time

TC = int(input())
for test_case in range(1,TC+1):
    cacheSize = int(input())
    cities = list(input().split())
    answer =my(cacheSize,cities)
    print(answer)