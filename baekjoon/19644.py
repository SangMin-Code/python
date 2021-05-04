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
    flag = True
    start = -r+1
    end = 0
    bomb = r-1
    shoot_dam = 0
    full_dam =r*d
    bomber = [False]*l

    for idx,life in enumerate(jombies):
        shoot_dam = full_dam - bomb*d
        if(shoot_dam<life):
            if g <=0:
                flag=False
                break
            g -=1
            bomb+=1
            bomber[end]=True
        if start<0 or bomber[start]:
            bomb-=1
        start+=1
        end+=1
        if end ==l:
            break

    return "YES" if flag else "NO"

TC = int(input())
for test_case in range(1, TC + 1):
    l = int(sys.stdin.readline().rstrip())
    r,d = map(int,sys.stdin.readline().rstrip().split())
    g = int(sys.stdin.readline().rstrip())
    jombie = [int(sys.stdin.readline().rstrip()) for _ in range(l)]
    answer = my(l,r,d,g,jombie)
    print(answer)
