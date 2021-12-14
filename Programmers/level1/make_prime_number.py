import sys
from typing import List
from itertools import combinations

sys.stdin = open('Programmers/level1/input/make_prime_number.text')


def solution(nums: List) -> int:
    answer = 0
    comb = combinations(nums, 3)
    for i in comb:
        if isPrime(sum(i)):
            answer += 1
    return answer


def isPrime(num: int) -> bool:
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
    return True


TC = int(input())
for i in range(TC):
    nums = list(map(int, input().split()))
    result = solution(nums)
    print(result)
