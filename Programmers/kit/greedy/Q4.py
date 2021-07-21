# Q4.py
import sys
from typing import List

sys.stdin = open('input/Q4')


def my(people:List[int],limit:int)->int:
    answer =0
    people.sort()
    left,right = 0, len(people)-1
    while left<=right:
        if people[left]+people[right]>limit:
            answer+=1
            right-=1
        else:
            left+=1
            right+=1
            answer+=1
    return answer


TC = int(input())
for test_case in range(1, TC + 1):
    people = list(map(int,input().split()))
    limit = int(input())
    answer = my(people,limit)
    print(answer)
