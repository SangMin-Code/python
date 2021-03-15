#travel_length.py
import sys
sys.stdin=open('input/travel_length')
from typing import List
import collections

def my(route:str)->int:
    visited = {'U':[],'D':[],'L':[],'R':[]}
    dic = { 'U':[0,1],'D':[0,-1],'L':[-1,0],'R':[1,0]}
    reverse = {'U':'D', 'D':'U', 'L':'R','R':'L'}
    count = 0
    current = [0,0]
    for d in route:
        dx,dy = current[0],current[1]
        nx,ny = dx+dic[d][0],dy+dic[d][1]
        if -5<=nx<=5 and -5<=ny<=5:
            if [dx,dy] not in visited[d] \
                and [nx,ny] not in visited[reverse[d]]:  #반대로 가는길일경우
                count+=1
                visited[d].append([dx,dy])
                visited[reverse[d]].append([nx,ny])
            current=[nx,ny]
    return count


TC = int(input())
for test_case in range(1,TC+1):
    route = input()
    answer = my(route)
    print(answer)