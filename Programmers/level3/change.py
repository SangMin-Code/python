#change
import sys
sys.stdin=open('input/change')
from typing import List

def my(n:int, money:List)->int:
    # dp생성
    dp = [[0] * (n + 1) for _ in range(len(money))]
    # 각 열은 지불하는 액수, 각 행은 지불하는 동전의 종류들
    # [[0].[1],[2],[3],[4],[5]] - [1] 로 지불
    # [[0].[1],[2],[3],[4],[5]] - [1,2] 로 지불
    # [[0].[1],[2],[3],[4],[5]] - [1,2,5] 로 지불
    # 0원은 지불 가능하니까 1로 시작
    dp[0][0] = 1
    # 첫번째 금액으로 n원을 구성 가능하면 1로 변경
    for i in range(money[0], n + 1, money[0]):
        dp[0][i] = 1
    # y: 지불가능한 동전
    for y in range(1, len(money)):
        # x: 거슬러줘야하는 금액
        for x in range(n + 1):
            # 거슬러줘야하는 금액이 지불가능한 동전보다 클 경우
            if x >= money[y]:
                dp[y][x] = (dp[y - 1][x] + dp[y][x - money[y]]) % 1000000007
            # 반대의 경우
            else:
                dp[y][x] = dp[y - 1][x]
    # 마지막 값 출력
    return dp[-1][-1]

'''
    reg=[0]*(n+1)
    reg[0]=1
    for i in money:
        for j in range(i, n+1):
            reg[j]+=reg[j-i]
    return reg[n]
'''

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    money = list(map(int,input().split()))
    answer = my(n,money)
    print(answer)