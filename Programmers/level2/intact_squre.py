#https://programmers.co.kr/learn/courses/30/lessons/62048
#intact_squre.py
import sys
sys.stdin=open('input/intact_squre')
from typing import List
import math

def my(w:int, h:int)->int:
    answer = 0
    if w == h:
        return w ** 2 - w
    else:
        for i in range(1, w + 1):
            answer += math.ceil(h / w * i) - math.floor(h / w * (i - 1))
            print(math.ceil(h / w * i) - math.floor(h / w * (i - 1)))

    return w*h-answer

def solution(w:int,h:int)->int:
    return (w*h-(w+h-math.gcd(w,h)))

TC = int(input())
for test_case in range(1,TC+1):
    w,h = map(int,input().split())
    answer = my(w,h)
    print(answer)