#long_jump
import sys
sys.stdin=open('input/long_jump')
from typing import List

def my(n:int)->int:
    answer = 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    val1, val2 = 1, 2
    val = 0
    for i in range(n - 2):
        val = val1 + val2
        val2, val1 = val, val2
    answer = val

    return answer % 1234567

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    answer = my(n)
    print(answer)