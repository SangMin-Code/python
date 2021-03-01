import sys
sys.stdin = open('input/merge_intervals')
from typing import List


def my(imtervals:List[List[int]])->List[List[int]]:
    intervals.sort(key=lambda x:x[0])
    answer = []
    for i in intervals:
        if answer and i[0]<answer[-1][1]:
            answer[-1][1] = max(answer[-1][1],i[1])
        else :
            answer.append(i)
    return answer

def merge(intervals:List[List[int]])->List[List[int]]:
    merged = []
    for i in sorted(intervals, key = lambda x:x[0]):
        if merged and i[0]<=merged[-1][1]:
            merged[-1][1]=max(merged[-1][1],i[1])
        else:
            merged+=i,
            #merged+=[i]
    return merged


case = int(input())
intervals = []
for _ in range(case):
    nums = list(map(int,input().split()))
    intervals.append(nums)
answer =my(intervals)
print(answer)