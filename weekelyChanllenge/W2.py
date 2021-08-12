# W2.txt.py
import sys
from typing import List

sys.stdin = open('input/W2.txt')


def my(scores:List[List[int]])->str:
    result =''
    scores = convertColRow(scores)
    for idx,student in enumerate(scores):
        avg = getAvg(idx,student)
        result += getGrade(avg)
    return result

def convertColRow(list):
    n = len(list)
    new_list = [[0]*n for i in range(n)]

    for i,row in enumerate(list):
        for j,col in enumerate(row):
            new_list[j][i] = list[i][j]
    return new_list


def getAvg(idx,list:List[int]):
    my_score = list[idx]
    cnt = list.count(my_score)
    max_val,min_val = max(list),min(list)
    if cnt ==1 and (max_val==my_score or min_val==my_score):
        new_list= list[:]
        new_list.pop(idx)
        return sum(new_list)/len(new_list)
    return sum(list)/len(list)


def getGrade(score):
    if score>=90:
        return 'A'
    elif score>=80:
        return 'B'
    elif score>=70:
        return 'C'
    elif score>=50:
        return 'D'
    else :
        return 'F'

TC = int(input())
for test_case in range(1, TC + 1):
    scores = [list(map(int,i.split())) for i in input().split(',')]
    answer = my(scores)
    print(answer)
