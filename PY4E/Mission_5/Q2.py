import collections
import sys
from typing import List
sys.stdin=open('input/Q2',encoding='utf8')

def grader(answer_paper:List[List[str]],answer:List[str]):
    dic = []
    for student in answer_paper:
        name, paper = student
        dic.append([name,grade(paper,answer)])

    dic.sort(key=lambda x: x[1],reverse=True)

    for i,student in enumerate(dic):
        name,score = student
        print(f'학생:{name},점수:{score}점 {i+1}등')


def grade(paper:str,answer:List[str])->int:
    score = 0
    for i,v in enumerate(paper):
        if v== answer[i]:
            score+=10
    return score

answer_paper = [i.split(',') for i in input().split()]
answer = list(input().split(','))

grader(answer_paper,answer)
