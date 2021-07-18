# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q1')


def my(array:List[int],commands:List[List[int]])->List[int]:
    answer = []
    for i, j, k in commands:
        temp = sorted(array[i - 1:j])
        answer.append(temp[k - 1])

    return answer



TC = int(input())
for test_case in range(1, TC + 1):
    array = list(map(int,input().split()))
    commands = [list(int,i.split()) for i in list(input().split(','))]
    answer = my()
    print(answer)
