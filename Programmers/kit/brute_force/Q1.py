# Q1.py
import sys
from typing import List

sys.stdin = open('input/Q1')

def my(answers:List[int])->List[int]:
    types=[
        [1,2,3,4,5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    answer =[]
    scores = [0]*len(types)
    for i in range(len(answers)):
        for j,type in enumerate(types):
            if answers[i]==type[i%len(type)]:
                scores[j]+=1
    max_score = max(scores)

    for i in range(len(types)):
        if scores[i]==max_score:
            answer.append(i+1)

    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    answers = list(map(int,input().split()))
    answer = my(answers)
    print(answer)
