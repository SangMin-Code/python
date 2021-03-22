#n_base_game.py
import sys
sys.stdin=open('input/n_base_game')
from typing import List

def my(n:int, t:int, m:int, p:int)->str:
    idx = 0
    answer = []
    num = 0
    s = '0123456789ABCDEF'
    while True:
        convert_num =''
        for_con = num
        if for_con ==0:
            convert_num='0'
        while for_con>0:
            convert_num = s[for_con%n] + convert_num
            for_con = for_con//n
        for i,val in enumerate(convert_num):
            if (idx+i)%m+1 == p:
                answer.append(str(val))
            if len(answer) == t:
                return ''.join(answer)
        idx = idx+len(convert_num)
        num+=1

TC = int(input())
for test_case in range(1,TC+1):
    n,t,m,p = map(int,input().split())
    answer =my(n,t,m,p)
    print(answer)