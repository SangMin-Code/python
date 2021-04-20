#way_to_school.
#https://programmers.co.kr/learn/courses/30/lessons/42898
import sys
sys.stdin=open('input/way_to_school')
from typing import List

def my(m:int,n:int,puddles:List[List[int]])->int:
    ways = [[0] * (m + 1) for i in range(n + 1)]
    ways[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [j, i] in puddles:
                continue
            else:
                if ways[i][j - 1] not in puddles:
                    ways[i][j] += ways[i][j - 1]
                if ways[i - 1][j] not in puddles:
                    ways[i][j] += ways[i - 1][j]
    return ways[n][m] % 1000000007   #최단경로의 개수를 1,000,000,007로 나눈 나머지를 return

TC = int(input())
for test_case in range(1,TC+1):
    m,n = map(int,input().split())
    puddles = [list(map(int,i.split(','))) for i in list(input().split())]
    answer = my(m,n,puddles)
    print(answer)