# 11444.py
import sys
from typing import List

sys.stdin = open('input/11444')


def my(n: int) -> int:
    a, b = 0, 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(n):
            a, b = b, a + b
        return a % 1000000007


def my2(n: int) -> int:
    if n < 2:
        return n
    cache = [0] * (n + 1)
    cache[1] = 1
    for i in range(2, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]
    return cache[n] % 1000000007


def my3(n: int) -> int:
    def multiple(a: List[List[int]], b: List[List[int]]):
        m = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for l in range(2):
                    m[i][j] += a[i][l] * b[l][j]
        return m

    i_matrix = [[1 if i == j else 0 for i in range(2)] for j in range(2)]

    def divide(m, ex):
        if ex == 1:
            return multiple(m, i_matrix)
        elif ex == 2:
            return multiple(m, m)
        else:
            tmp = divide(m, ex // 2)
            if ex % 2 == 0:
                return multiple(tmp, tmp)
            else:
                return multiple(multiple(tmp, tmp), m)

    zero = [[1, 1], [1, 0]]

    return divide(zero, n)[0][1] % 1000000007


def my4(n: int) -> int:
    fi, result_m = [[1, 1], [1, 0]], [[1, 0], [0, 1]]

    def mul(a, b):
        new_m = [[0, 0], [0, 0]]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    new_m[i][j] += a[i][k] * b[k][j]
                new_m[i][j] %= 1000000007
        return new_m

    while n:
        if n % 2:
            result_m = mul(result_m, fi)
        fi = mul(fi, fi)
        n //= 2

    return result_m[0][1]


TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    answer = my4(n)
    print(answer)
