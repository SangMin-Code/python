#compression.py
#https://programmers.co.kr/learn/courses/30/lessons/17684
import sys
sys.stdin=open('input/compression')
from typing import List


def my(s:str)->List[int]:
    index_dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,
                 'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,
                 'X':24,'Y':25,'Z':26}
    idx = 0
    answer = []
    while idx <len(s):
        sub_idx = 1
        out = ''
        while s[idx:idx+sub_idx] in index_dic.keys() and idx+sub_idx <= len(s):
            out = index_dic[s[idx:idx+sub_idx]]
            sub_idx+=1
        if idx+sub_idx ==len(s):
            if s[idx:idx+sub_idx] in index_dic.keys():
                answer.append(out)
            else :
                answer.append(out)
                answer.append(index_dic[s[-1]])
            break
        index_dic[s[idx:idx+sub_idx]] = len(index_dic) + 1
        idx = idx+sub_idx-1
        answer.append(out)
    return answer



TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    answer = my(s)
    print(answer)