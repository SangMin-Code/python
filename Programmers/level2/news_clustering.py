#news_clustering.py
#https://programmers.co.kr/learn/courses/30/lessons/17677
import sys
sys.stdin=open('input/news_clustering')
from typing import List

def my(str1:str, str2:str)->int:
    str1 = str1.lower()
    str2 = str2.lower()

    str1_list=[]
    str2_list=[]

    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i]+str2[i+1])

    if not str1_list and not str2_list:
        return 1*65536

    #교집합
    for_inter = str2_list[:]
    cnt = 0
    for i in str1_list:
        if i in for_inter:
            for_inter.remove(i)
            cnt+=1

    #합집함
    union = len(str1_list)+len(str2_list)-cnt
    return int(cnt/union *65536)

TC = int(input())
for test_case in range(1,TC+1):
    str1=input()
    str2=input()
    answer = my(str1,str2)
    print(answer)