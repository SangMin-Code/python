# 17245.py
import sys
from typing import List

sys.stdin = open('input/17245')


def my(n:int, servers:List[List[int]],total:int,max_val:int)->int:
    def count(num):
        cnt = 0
        for i in range(n):
            for j in range(n):
                if servers[i][j]>=num:
                    cnt+=num
                else:
                    cnt += servers[i][j]
        return cnt

    left,right = 0, max_val
    result = 0
    while left<=right:
        mid = left+ (right-left)//2
        if count(mid)>=total/2:
            right = mid-1
            result = mid
        else:
            left = mid+1
    return result

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    servers = []
    total = 0
    max_val = 0
    for i in range(n):
        temp = list(map(int,sys.stdin.readline().rstrip().split()))
        servers.append(temp)
        total+=sum(temp)
        max_val = max(max(temp),max_val)
    answer = my(n,servers,total,max_val)
    print(answer)
