#https://programmers.co.kr/learn/courses/30/lessons/12924
#number_expression.py
import sys
sys.stdin=open('input/number_expression')
from typing import List

def my(n:int):
    answer = 0
    idx = 1
    while (n // idx >= idx // 2):
        if idx % 2 != 0 and n%idx ==0:
            answer += 1
        elif idx % 2 == 0 and (n - idx // 2) % idx == 0:
            answer += 1
        idx += 1
    return answer

def practice(n:int):
    answer = 0
    idx = 1
    while (n//idx >=idx//2):
        if idx%2 !=0 and n%idx==0:
            answer +=1
        elif idx%2==0 and (n-idx//2)%idx==0:
            answer+=1
        idx+=1
    return answer
TC = int(input())
for test_case in range(1,TC+1):
 num =int(input())
 print(my(num))