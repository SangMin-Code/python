#rangking
#https://programmers.co.kr/learn/courses/30/lessons/49191
import sys
sys.stdin=open('input/rangking')
from typing import List
import collections
def my(n:int, results:List[List[int]])->int:
    answer = 0
    wins = collections.defaultdict(set) # i 선수가 이긴 목록
    loses = collections.defaultdict(set) # i 선수가 진 목록

    for win,lose in results:
        wins[win].add(lose)
        loses[lose].add(win)

    for i in range(1,n+1):
        for winner in loses[i]:         #i 선수에게 이긴 선수들은 i 선수가 이긴 선수들보다 실력이 높음
            wins[winner].update(wins[i])
        for loser in wins[i]:           # i 선수에게 진 선수들은 i 선수가 진 선수들보다 실력이 낮음
            loses[loser].update(loses[i])

    for i in range(1,n+1):              # 자신을 제외한 모든 정보를 가지고 있으면 랭킹을 알 수 있음
        if len(wins[i])+len(loses[i])==n-1:
            answer+=1
    return answer




TC = int(input())
for test_case in range(1,TC+1):
    n=int(input())
    results = [list(map(int,i.split())) for i in list(input().split(','))]
    answer = my(n,results)
    print(answer)