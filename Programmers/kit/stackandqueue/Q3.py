# Q1.py
import collections
import sys
from typing import List

sys.stdin = open('input/Q3')


def my(bridege_length:int, weight:int, truck_weights:List[int])->int:
    answer = 0
    bridege = collections.deque([0]*bridege_length)
    truck_weights =collections.deque(truck_weights)
    sum =0

    while bridege:
        answer+=1
        sum -= bridege.popleft()
        if truck_weights:
            if sum+truck_weights[0]<=weight:
                bridege.append(truck_weights.popleft())
                sum+=bridege[-1]
            else:
                bridege.append(0)
    return answer

def my2(bridege_length:int, weight:int, truck_weights:List[int])->int:
    time = 1
    passing_truck = []
    passed_truck = []
    current_weight = 0
    time_dic = collections.defaultdict(int)

    while True:
        while truck_weights:
            if weight>= current_weight+truck_weights[0]:
                passing_truck.append(truck_weights.pop(0))
                time_dic[time]=bridege_length+time
                current_weight = sum(passing_truck)
            break

        time +=1

        if time in time_dic.values():
            passed_truck.append(passing_truck.pop(0))

        current_weight = sum(passing_truck)

        if not passing_truck and not truck_weights:
            return time

def my3(bridege_length: int, weight: int, truck_weights: List[int]) -> int:
    queue = []
    seconds = 1
    total_weights = 0
    for truck in truck_weights:
      if not queue:
        queue.append((truck, seconds))
        total_weights += truck
      else:
        if(total_weights+truck <= weight):
          seconds += 1
          queue.append((truck, seconds))
          total_weights += truck
        else:
          while(total_weights+truck > weight):
            seconds = queue[0][1]+bridge_length
            if(queue[0][1]+bridge_length > queue[-1][1]): seconds = queue[0][1]+bridge_length
            else: seconds = queue[-1][1]+1
            total_weights -= queue[0][0]
            queue.pop(0)
          queue.append((truck, seconds))
          total_weights += truck

    if queue:
      seconds = queue[-1][1]+bridge_length

    answer = seconds

    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    bridge_length,weight = map(int,input().split())
    truck_weights = list(map(int,input().split()))
    answer = my2(bridge_length,weight,truck_weights)
    print(answer)
