'''
연쇄행렬곱셈 알고리즘

행렬의 곱은 결합법칙이 성립하기 때문에
연속적인 행렬의 곱은 결과는 같으나
결합을 어떻게 하느냐에 따라 연산 횟수가 달라진다.
순서는 일정하나 결합순서에 따라 연산 횟수가 달라질 때 사용하는 알고리즘

방법
1. 구하고자 하는 행렬 순서가 다음과 같을 때
    (5,3) (3,2) (2,6)
    행렬 곱 계수를 구한다.
    d =[5,3,2,6]

2. dp의 이중배열을 이용해 start에서 end까지의
   최솟값을 구하여 저장한다.
   ex) 행렬 A*B*C
    (1,3) -> min((1,2)*3+d, 1*(2,3)+d)

3. 행렬의 최솟값을 구하는 점화식은 다음과 같다.
    i,j,k = 시작점, 끝나는점, k 중간지점
    dp[i][j] = min( d[i][k] + d[k+1][j] + d[i-1]*d[k] *d[j])

    뒤의 곱은 행렬계산시 곱셈 횟수
4. dp[1][n]을 return

'''

import sys
from typing import List

sys.stdin = open('input/matirxChainMultiplication')
def my(n:int, matrix:List[List[int]])->int:
    dp = [[0]*(n+1) for _ in range(n+1)]
    d=[]
    for i,j in matrix:
        d.append(i)
    d.append(matrix[-1][-1])
    for l in range(2,n+1):
        for i in range(1,n-l+2):
            j=i+l-1
            dp[i][j]= min([dp[i][k]+dp[k+1][j]+d[i-1]*d[k]*d[j] for k in range(i,j)])
    return dp[1][n]

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    matrix = [list(map(int,input().split())) for _ in range(n)]
    answer = my(n,matrix)
    print(answer)