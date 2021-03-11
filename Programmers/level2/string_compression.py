#https://programmers.co.kr/learn/courses/30/lessons/60057
#string_compression.py
import sys
sys.stdin=open('input/string_compression')
from typing import List

def my(s:str)->int:
    stack = []
    min_length = len(s)
    for i in range(1,len(s)//2+1):
        comp_str = ""
        left, right = 0,i
        stack.append(s[left:right])
        left,right = left+i,right+i
        cnt = 1
        while right <=len(s):
            if stack[-1] == s[left:right]:  #스택과 동일한 문자일때
                cnt+=1
            else :                          #스택과 다른 문자일때
                if cnt!=1:  #반복이 두번이상
                    comp_str += str(cnt)+stack.pop()
                else:       #반복 한번
                    comp_str+=stack.pop()
                cnt =1
                stack.append(s[left:right])
            left, right = left + i, right + i
        if cnt != 1:  # 반복이 있을때
            comp_str += str(cnt) + stack.pop() +s[left:]
        else:
            comp_str += stack.pop()+s[left:]
        min_length = min(min_length, len(comp_str))
    return min_length

def practice(s:str)->int:
    min_length = len(s)
    for i in range(1,len(s)//2+1):
        stack=[]
        part = ''
        cnt =1
        left,right = 0,i
        while left<len(s)+i:
            if stack:
                if stack[-1]==s[left:right]:
                    cnt+=1
                else :
                    if cnt>1:
                        part +=str(cnt)
                    part+=stack.pop()
                    cnt=1
                    stack.append(s[left:right])
            else :
                stack.append(s[left:right])
            left, right = left + i, right + i
        min_length=min(min_length,len(part))
    return min_length







TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    #answer = my(s)
    answer = practice(s)
    print(answer)