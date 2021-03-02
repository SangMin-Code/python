#gas_station
import sys
sys.stdin = open('input/gas_station')
from typing import List

#leetCode : 134

def my(gas:List[int], cost:List[int])->int:
    def find(idx:int):
        current_gas = 0
        for i in range(len(gas)): #모든 주유소를 통과
            idx = (idx+i)%len(gas)  # 주유소 배치가 원형
            current_gas += gas[idx]
            if current_gas - cost[idx]<0: #기름이 0까지 소모
                return False
        return True
    for i in range(len(gas)):
        if find(i):
            return i #출발점이 유일하므로
    return -1

def visit_all(gas:List[int],cost:List[int])->int:
    for start in range(len(gas)):
        fuel =0
        for i in range(start, len(gas)+start):
            index = i%len(gas)

            can_travel = True
            if gas[index]+fuel<cost[index]:
                can_travel=False
                break
            else:
                fuel+=gas[index]-cost[index]
        if can_travel:
            return start
    return -1

def visit_once(gas:List[int], cost:List[int])->int:
    #출발점이 유일하므로 출발점은 반드시 한 군데만 존재
    if sum(gas)<sum(cost):
        return False
    '''
    전체를 방문하면서 성립되지 않는 경우는 출발점을 한 칸씩 밀어낸다.
    한 번 이상은 반드시 성립되지 않는 지점이 존재하고 성립되지 않는 지점이 있으면
    그 앞은 전부 출발점이 될 수 없다. 
    '''
    start, fuel = 0, 0
    for i in range(len(gas)):
        #출발점이 안 되는 지점 판별
        if gas[i]+fuel<cost[i]:
            start=i+1
            fuel=0
        else:
            fuel+=gas[i]-cost[i]
    return start

gas = list(map(int,input().split()))
cost = list(map(int,input().split()))
answer = my(gas,cost)
print(answer)