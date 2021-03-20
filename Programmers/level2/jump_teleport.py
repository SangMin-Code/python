#https://programmers.co.kr/learn/courses/30/lessons/12980?language=python3
#jump_teleport.py
import sys
sys.stdin=open('input/jump_teleport')
from typing import List

def my(n:int)->int:
    return bin(n).count('1')

TC = int(input())
for test_case in range(1,TC+1):
    n= int(input())
    answer = my(n)
print(answer)