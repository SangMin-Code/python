#trucks_criossing_bridge.py
import sys
sys.stdin=open('input/trucks_criossing_bridge')
from typing import List
import collections

def my(bridege_length:int, weight:int, truck_weights:List[int])->int:
    time = 0
    bridge = collections.deque([0]*bridege_length)
    truck_weights = collections.deque(truck_weights)
    while len(bridge)!=0:
        time+=1
        bridge.popleft()
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return time

TC = int(input())
for test_case in range(1,TC+1):
    bridege_length = int(input())
    weight = int(input())
    truck_weights = list(map(int,input().split()))
    answer = my(bridege_length,weight,truck_weights)
    print(answer)