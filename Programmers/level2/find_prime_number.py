#https://programmers.co.kr/learn/courses/30/lessons/42839
#소수 찾기

import sys
sys.stdin = open('input/find_prime_number')
from typing import List
import math
import itertools

def my(numbers:str)->int:
    def is_prime(num:int):
        flag = True
        for i in range(2, int(math.sqrt(float(num))),1):
            if num%i==0:
                return False
        return flag
    #완전탐색
    nums = []
    prev_elements =[]
    def dfs(elements,n):
        if len(prev_elements) ==n:
            candidate = int(''.join(prev_elements))
            if is_prime(candidate) and candidate>1:
                nums.append(candidate)
        elif len(prev_elements)<n:
            for e in elements:
                next_elments = elements[:]
                next_elments.remove(e)
                prev_elements.append(e)
                dfs(next_elments,n)
                prev_elements.pop()
    for i in range(len(numbers)):
        dfs(list(numbers),i+1)
    nums = list(set(nums))
    return len(nums)

def practice(number:str)->int:
    def is_prime(n):
        for i in range(2,int(n**0.5)+1,1):
            if n%i==0:
                return False
        return True
    #순열
    nums =[]
    prev_elments = []
    def dfs(elments,n):
        if len(prev_elments)==n:
            candidate = int(''.join(prev_elments))
            if is_prime(candidate) and candidate>1:
                nums.append(candidate)
        elif len(prev_elments)<n:
            for e in elments:
                next_elements = elments[:]
                next_elements.remove(e)
                prev_elments.append(e)
                dfs(next_elements,n)
                prev_elments.pop()

    stack = []
    answer = []
    candidates = list(numbers)






    if not number :
        return 0
    for i in range(len(numbers)):
        dfs(list(numbers),i+1)
    nums = list(set(nums))
    return len(nums)


def solution_1(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, itertools.permutations(list(n), i + 1)))) #각 길이별 조합 구학
    a -= set(range(0, 2)) #0,1 은 소수에서 제외
    for i in range(2, int(max(a) ** 0.5) + 1): # 약수가 될 수 있는 수의 범위
        a -= set(range(i * 2, max(a) + 1, i))  # 최초의 i 이후 배수들 제거
    return len(a)
    #에라토스테네스 체 -> 구간에서 약수들을 모두 제거하여 소수를 찾는 방법




TC = int(input())
for test_case in range(1,TC+1):
    numbers = input()
    #answer = my(numbers)
    answer = solution_1(numbers)
    print(answer)