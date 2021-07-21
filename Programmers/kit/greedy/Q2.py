# Q2.py
import sys
from typing import List

sys.stdin = open('input/Q2')


def my(name:str)->int:
    answer,idx = 0,0

    list = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]

    while True:
        answer+=list[idx]
        list[idx]=0
        if sum(list)==0:
            return answer
        left,right = 1,1
        while list[idx-left]==0:
            left+=1
        while list[idx+right]==0:
            right+=1

        if left<right:
            answer+=left
            idx-=left
        else:
            answer+=right
            idx+=right




TC = int(input())
for test_case in range(1, TC + 1):
    name = input()
    answer = my(name)
    print(answer)
