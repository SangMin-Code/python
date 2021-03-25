#Q7.py
import sys
sys.stdin=open('input/Q7')
from typing import List

def my(logs:List[int])->int:
    convert = []
    for i,v in enumerate(logs):
        day,hh,width = v.split(' ')
        width = width[:-1]
        h,m,s =  map(float,hh.split(':'))

TC = int(input())
for test_case in range(1,TC+1):
    logs = list(input().split(','))
    answer  = my(logs)
    print(answer)


    #test