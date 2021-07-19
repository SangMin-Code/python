# Q2.py
import functools
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(numbers:List[int])->str:
    numbers = list(map(str,numbers))
    numbers.sort(key= lambda x:x*3, reverse=True)
    flag = False
    for i in numbers:
        if i != '0':
            flag = True
    if flag:
        return ''.join(numbers)
    else:
        return '0'

def my2(numbers:List[int])->str:
    def comporator(a,b):
        t1 = a+b
        t2 = b+a
        return (int(t1)>int(t2))-(int(t1)<int(t2))
    def sol(numbers):
        n = list(map(str,numbers))
        n = sorted(n,key=functools.cmp_to_key(comporator),reverse=True)
        answer = str(int(''.join(n)))
        return answer
    return sol(numbers)

TC = int(input())
for test_case in range(1, TC + 1):
    numbers = list(map(int,input().split()))
    answer = my2(numbers)
    print(answer)
