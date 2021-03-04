import sys
sys.stdin = open('input/lifeboat')
from typing import List
#https://programmers.co.kr/learn/courses/30/lessons/42885


def my(people:List[int], limit:int)->int:
    answer = 0
    people.sort()
    left,right = 0, len(people)-1
    while left <= right :
        print(left,right)
        if people[left]+people[right]>limit:
            answer +=1
            right-=1
        else:
            answer +=1
            left+=1
            right-=1
    print(answer)


TC = int(input())
for test_case in range(1,TC+1):
    limit = int(input())
    people = list(map(int,input().split()))
    my(people,limit)