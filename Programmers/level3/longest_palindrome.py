#https://programmers.co.kr/learn/courses/30/lessons/12904
#longest_palindrome.py
import sys
sys.stdin=open('input/longest_palindrome')
from typing import List

def my(s:str)->int:
    for cut in range(len(s), 0, -1):
        for start in range(0, len(s)-cut+1):
            cutStr = s[start:start + cut]
            if cutStr == cutStr[::-1]:
                return len(cutStr)

TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    answer = my(s)
    print(answer)