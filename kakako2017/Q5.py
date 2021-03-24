#Q5.py
import sys
sys.stdin=open('input/Q5')
from typing import List

def my(str1:str, str2:str)->int:
    str1_list = []
    str2_list = []
    answer = 1
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i:i+2].lower())
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i:i+2].lower())

    for_inter = str1_list[:]
    inter = 0
    for str in str2_list:
        if str in for_inter:
            for_inter.remove(str)
            inter+=1
    union =len(str1_list)+len(str2_list)-inter

    if inter==0:
        answer = 1*65536
    else :
        answer = inter/union*65536
    return int(answer)

TC = int(input())
for test_case in range(1,TC+1):
    str1 = input()
    str2 = input()
    answer = my(str1,str2)
    print(answer)