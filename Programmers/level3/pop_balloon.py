# pop_balloon.py
#https://programmers.co.kr/learn/courses/30/lessons/68646
import sys

sys.stdin = open('input/pop_balloon')
from typing import List


def my(a: List[int]) -> int:
    answer = 0
    left_min = 10000000001
    right_min = min(a)
    idx = a.index(right_min)

    for i in range(0,idx):
        if i==0:
            answer+=1
        else:
            if a[i]<left_min or a[i]<right_min:
                answer+=1
        left_min = min(left_min,a[i])

    left_min = min(a)
    right_min = 10000000001
    for i in range(len(a)-1, idx,-1):
        if i==len(a)-1:
            answer+=1
        else :
            if a[i]<right_min or a[i]<left_min:
                answer+=1
        right_min = min(right_min,a[i])
    return answer+1


TC = int(input())
for test_case in range(1, TC + 1):
    balloons = list(map(int, input().split()))
    answer = my(balloons)
    print(answer)
