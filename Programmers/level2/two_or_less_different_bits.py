import sys
from typing import List
sys.stdin = open('Programmers/level2/input/two_or_less_different_bits.txt')


def solution(numbers: List[int]) -> List[int]:

    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num+1)
        else:
            bin_num = '0'+bin(num)[2:]
            one_idx = bin_num.rfind('0')
            bin_num = list(bin_num)
            bin_num[one_idx] = '1'
            bin_num[one_idx+1] = '0'
            answer.append(int(''.join(bin_num), 2))

    return answer


TC = int(input())
for i in range(TC):
    numbers = list(map(int, input().split()))
    result = solution(numbers)
    print(result)
