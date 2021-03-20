#expression_maximization.py
import sys
sys.stdin=open('input/expression_maximization')
from typing import List
import collections

#eval
def my(expression:str)->int:
    def calc(priority, n, expression):
        if n == 2:
            return str(eval(expression))
        if priority[n] == '*':
            res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
        if priority[n] == '+':
            res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
        if priority[n] == '-':
            res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
        return str(res)

    answer = 0
    priorities = [
            ('*', '-', '+'),
            ('*', '+', '-'),
            ('+', '*', '-'),
            ('+', '-', '*'),
            ('-', '*', '+'),
            ('-', '+', '*')
        ]
    for priority in priorities:
        res = int(calc(priority, 0, expression))
        answer = max(answer, abs(res))

    return answer

TC = int(input())
for test_case in range(1,TC+1):
    expression = input()
    answer = my(expression)
    print(answer)