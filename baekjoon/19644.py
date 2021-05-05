# 19644.py
import collections
import sys
from typing import List
import collections
sys.stdin = open('input/19644')

'''
시간초과 
def my(l:int,r:int,d:int,g:int,jombies:List[int])->str:
    window = collections.deque(maxlen=r)
    for idx,i in enumerate(jombies):
        window.append(1)
        if sum(window)*d <i:
            if g<=0:
                return 'NO'
            else :
                g-=1
                window[-1]=0
    return 'YES'
'''
def my(l:int,r:int,d:int,g:int,jombies:List[int])->str:
    # l: 좀비 list 길이, r: 사거리 d: 데미지 g: 수류탄 수, jombies: 좀비 체력 리스트
    #[? ? ?] r 크기의 윈도우를 움직이면서 윈도우 내의 정보로 end위치의 좀비 대응을 결정,
    # end 좀비 대응 후 start,end를 이동시켜 진행
    start=-r+1
    end =0
    bomb = r-1
    is_bomb = [False]*l

    for life in jombies:
        damage = (r-bomb)*d
        if damage<life:
            if g<=0:
                return 'NO'
            g-=1
            bomb+=1
            is_bomb[end]=True
        if start<0 or is_bomb[start]:
            bomb-=1
        start+=1
        end+=1
    return 'YES'

TC = int(input())
for test_case in range(1, TC + 1):
    l = int(sys.stdin.readline().rstrip())
    r,d = map(int,sys.stdin.readline().rstrip().split())
    g = int(sys.stdin.readline().rstrip())
    jombie = [int(sys.stdin.readline().rstrip()) for _ in range(l)]
    answer = my(l,r,d,g,jombie)
    print(answer)
