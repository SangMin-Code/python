#expression_with_N.py
#https://programmers.co.kr/learn/courses/30/lessons/42895
import sys
sys.stdin=open('input/expression_with_N')
from typing import List

def my(N:int, number:int)->int:
    s = [set() for _ in range(8)] #숫자 최대 사용횟수가 8개까지
    for i,x in enumerate(s):
        x.add(int(str(N)*(i+1))) # 사칙연산 없이 구하는 숫자
    s[1].add(N*N)     #2개의 숫자로 만들 수 있는 숫자
    s[1].add(N/N)
    s[1].add(N+N)
    s[1].add(N-N)

    for i in range(2,8):   # N개의 숫자로 만들 수 있는 숫자는 N-1개, N-2개 숫자가 가지는 숫자의 사칙연산으로 구함
        for j in range(i):
            for k in s[j]:      #  s(4) -> s(1),s(3), s(2),s(2), s(3)(3)의 사칙연산
                for l in s[i-j-1]:
                    s[i].add(k+l)
                    s[i].add(k-l)
                    s[i].add(k*l)
                    if l!=0:    # 분모가 0일경우 error
                        s[i].add(k//l)

    for i,val in enumerate(s):
        if number in val:
            return i+1
    return -1

TC = int(input())
for test_case in range(1,TC+1):
    N,number = map(int,input().split())
    answer = my(N,number)
    print(answer)