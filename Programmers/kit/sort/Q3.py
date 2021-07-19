# Q3.py
import sys
from typing import List

sys.stdin = open('input/Q3')


def my(citations:List[int])->int:
    citations.sort()
    answer = 0
    for i in range(len(citations)):
        citation = citations[len(citations)-1-i]
        if i+1 <= citation and citation>0:
            answer= i+1
    return answer




TC = int(input())
for test_case in range(1, TC + 1):
    citations = list(map(int,input().split()))
    answer = my(citations)
    print(answer)
