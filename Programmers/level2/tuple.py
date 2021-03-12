#tuple.py
#https://programmers.co.kr/learn/courses/30/lessons/64065
import sys
sys.stdin=open('input/tuple')
from typing import List
import collections

def my(s:str)->List[int]:
    s= s.replace('{','')
    s= s.replace('}','')
    list= s.split(',')
    cnt = collections.Counter(list).most_common()
    answer = []
    for i,v in cnt:
        answer.append(int(i))
    return answer




TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    answer = my(s)
    print(answer)