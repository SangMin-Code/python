# 17225.py
import sys
from typing import List

sys.stdin = open('input/17225')


def my(b:int, r:int, n:int, package:List[str])->List[List[int]]:

    b_order =[]
    r_order = []
    b_time,r_time =0,0
    for t,c,a in package:
        if c == "B":
            b_time = max(b_time,int(t))
            for i in range(int(a)):
                b_order.append([b_time,"B"])
                b_time+=b
        else :
            r_time = max(r_time, int(t))
            for i in range(int(a)):
                r_order.append([r_time,"R"])
                r_time+=r
    order = b_order+r_order
    order = sorted(order,key = lambda x: [x[0],x[1]])

    b_answer,r_answer = [],[]
    for i,v in enumerate(order):
        if v[1]=='B':
            b_answer.append(i+1)
        else :
            r_answer.append(i+1)

    print(len(b_answer))
    print(' '.join([str(i) for i in b_answer]))
    print(len(r_answer))
    print(' '.join([str(i) for i in r_answer]))

TC = int(input())
for test_case in range(1, TC + 1):
    b,r,n = map(int,sys.stdin.readline().rstrip().split())
    package = []
    for _ in range(n):
        package.append(list(sys.stdin.readline().rstrip().split()))
    my(b,r,n,package)

