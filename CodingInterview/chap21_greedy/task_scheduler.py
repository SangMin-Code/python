import sys
sys.stdin =open('input/task_scheduler')
from typing import List
import collections


def least_interval(tasks:List[str],n:int)->int:
    conter = collections.Counter(tasks)
    result = 0
    while True:
        sub_count=0
        for task,_ in conter.most_common(n+1):
            sub_count+=1
            result+=1
            conter.subtract(task)
            #0 이하인 아이템을 목록에서 완전히 제거
            conter+=collections.Counter()
        if not conter :
            break
        result+= n-sub_count+1
    return result



n=int(input())
tasks = list(input().split())
answer = least_interval(tasks,n)
