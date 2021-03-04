#https://programmers.co.kr/learn/courses/30/lessons/43165
import sys
from typing import List
sys.stdin = open('input/make_target_number')

def my(numbers:List[int], t:int)->int:
    answer =0
    def dfs(sum,k):
        if k == len(numbers):
            if sum ==t:
                return 1
            else :
                return 0
        else :
            return dfs(sum+numbers[k],k+1)+dfs(sum-numbers[k],k+1)
    return dfs(0,0)

    #iterator로 어덯게?

TC = int(input())
for test_case in range(1,TC+1):
    t = int(input())
    numbers = list(map(int,input().split()))
    answer = my(numbers,t)
    print(answer)