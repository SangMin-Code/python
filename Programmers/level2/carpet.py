#https://programmers.co.kr/learn/courses/30/lessons/42842
import sys
sys.stdin = open('input/carpet')
from typing import List

#격자무늬니까 항상 직사각형 형태인건가
def my(b:int, y:int)->List[int]:
    for i in range(1,yellow+1):
        width = i
        if yellow%i!=0:
            continue
        height = y//width
        if brown == 2*(width+2)+2*height:
            a = max(width,height)+2
            b = min(width,height)+2
            return(a,b)
    return -1



TC = int(input())
for test_case in range(1,TC+1):
    brown,yellow = map(int,input().split())
    answer =my(brown,yellow)
    print(answer)