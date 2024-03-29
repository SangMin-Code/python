#Q4.py.py
import sys
sys.stdin=open('input/Q4')
from typing import List

def my(n:int,t:int,m:int,timetable:List[str])->str:
    answer = 0
    convert_time = []
    for time in timetable:
        hour, minute = map(int,time.split(':'))
        convert_time.append(hour*60+minute)
    convert_time.sort()
    current = 540
    for _ in range(n):
        for _ in range(m):
            if convert_time and convert_time[0]<=current:
                answer = convert_time.pop(0)-1
            else :
                answer = current
        current+=t
    hour = str(answer//60)
    minute = str(answer%60)
    if len(hour)<2:
        hour = '0'+hour
    if len(minute)<2:
        minute ='0'+minute
    return hour+':'+minute

def solution(n:int,t:int,m:int,timetable:List[str])->str:
    answer = 0
    timetable = [int(time[:2])*60+int(time[3:]) for time in timetable]
    timetable.sort()
    current = 540
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0]<=current:
                answer = timetable.pop(0)-1
            else :
                answer =current
        current+=t
    h,m = divmod(answer,60)
    return str(h).zfill(2)+":"+str(m).zfill(2)

TC = int(input())
for test_case in range(1,TC+1):
    n,t,m = map(int,input().split())
    timetable = list(input().split())
    #answer =my(n,t,m,timetable)
    answer = solution(n, t, m, timetable)
    print(answer)
