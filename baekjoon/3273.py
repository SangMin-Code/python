# 3273.py
import collections
import sys
from typing import List

sys.stdin = open('input/3273')


def my(n:int,sequnece:List[int],x:int)->int:
    p1,p2,cnt = 0,0,0
    while p1<n:
        if sequnece[p1]>=x:
            continue
        p2 = p1+1
        while p2<n:
            if sequnece[p1]+sequnece[p2] == x:
                cnt +=1
                break
            p2+=1
        p1+=1
    return cnt

def my2(n:int,sequnece:List[int],x:int)->int:
    dic = collections.defaultdict(int)
    for i,v in enumerate(sequnece):
        dic[v]=i+1
    cnt = 0
    for i,v in enumerate(sequnece):
        if dic[x-v] > i+1:
            cnt+=1
    return cnt

def my3(n:int,sequnece:List[int],x:int)->int:
    check = [0]*2000001
    for i,v in enumerate(sequnece):
        check[v]=i
    cnt = 0
    for i,v in enumerate(sequnece):
        if x-v>0 and check[x-v]>i:
            cnt+=1
    return cnt


TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    sequence = list(map(int,sys.stdin.readline().rstrip().split()))
    x = int(sys.stdin.readline().rstrip())
    answer = my3(n,sequence,x)
    print(answer)
