# 10942.py
import sys
# from typing import List
#
sys.stdin = open('input/10942')
#
#
# def my(N:int,M:int,nums:List[int],a:List[List[int]])->List[int]:
#     answer = []
#     for s,e in a:
#         if(nums[s-1:e]==nums[s-1:e][::-1]):
#             answer.append(1)
#         else:
#             answer.append(0)
#     return answer
#
# def my2(N:int,M:int,nums:List[int],a:List[List[int]])->List[int]:
#     answer = []
#     dp = [[1 if i==j else 0 for j in range(N+1) ]for i in range(N+1)]
#     for l in range(2,N):
#         for s in range(1,N-l+1):
#             e = s+l
#             if nums[s-1]==nums[e-1] and dp[s + 1][e - 1]:
#                 dp[s][e]=1
#     for s,e in a:
#         answer.append(dp[s][e])
#     return answer
#
# TC = int(input())
# for test_case in range(1, TC + 1):
#     N = int(input())
#     nums = list(map(int,input().split()))
#     M = int(input())
#     a = []
#     for i in range(M):
#         a.append(list(map(int,input().split())))
#     answer = my2(N,M,nums,a)
#     for i in answer:
#         print(i)


#import sys

N=int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
dp = [[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    dp[i][i]=1
    if i<N and nums[i-1]==nums[i]:
        dp[i][i+1]=1

for l in range(2,N):
    for s in range(1,N-l+1):
        e = s+l
        if nums[s-1]==nums[e-1] and dp[s+1][e-1]==1:
            dp[s][e]=1

M=int(sys.stdin.readline().rstrip())
for _ in range(M):
    S,E = map(int,sys.stdin.readline().rstrip().split())
    print(dp[S][E])

