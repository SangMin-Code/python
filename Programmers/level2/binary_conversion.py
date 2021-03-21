#binary_conversion.py
#programmers.co.kr/learn/courses/30/lessons/70129
import sys
sys.stdin=open('input/binary_conversion')
from typing import List

def my(s:str)->List[int]:
    try_cnt, zero_cnt = [0,0]

    while s!='1':
        zero_cnt+= s.count('0')
        s = s.replace('0','')
        s= bin(len(s))[2:]
        try_cnt+=1

    return [try_cnt,zero_cnt]

def practice(s:str)->List[int]:
    try_cnt, zero_cnt =0,0

    while s!='1':
        zero_cnt+=s.count('0')
        s=s.replace('0','')
        s=bin(len(s))[2:]
        try_cnt+=1
    return [try_cnt,zero_cnt]


TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    answer = my(s)
    print(answer)
