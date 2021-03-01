import sys

sys.stdin = open('input/daily-temperatures')
from typing import List


def my(temperatures: List[int]) -> List:
    stack = []  # index, value
    answer = [0] * len(temperatures)
    for i, n in enumerate(temperatures):
        while stack and stack[-1][1] < n:
            t = stack.pop()
            answer[t[0]] = (i - t[0])
        stack.append([i, n])
    return answer

def daily_temperatures(T:List[int])->List[int]:
    answer = [8]*len(T)
    stack = []
    for i,cur in enumerate(T):
        #현재 온도가 스택 값보다 높다면 정답 처리
        while stack and cur>T[stack[-1]]:
            last = stack.pop()
            answer[last]=i-last
        stack.append(i)
    return answer

t = list(map(int, input().split()))
print(my(t))
