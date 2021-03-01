#Palindrome.py
'''
팰린드롬 : 앞뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장. 회문 이라고 부름
'''
import sys
import timeit
import collections
from typing import *
import typing

sys.stdin = open('input/Palindrome','r')

def my(s:str) ->bool:
    strs=[]
    for char in s:
        if char.isalnum():
            strs.append(char.lower()) #문자,숫자 외 제거
    flag = True
    for i in range(len(strs)//2):
        if strs[i]!=strs[len(strs)-1-i]:
            flag=False
            break
    print(flag)

def toList(s:str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())  # 문자,숫자 외 제거
    while len(strs)>1:
        if strs.pop(0)!=strs.pop():
            return False
    return True

def toDeque(s:str)->bool:
    strs: Deque = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char.lower())  # 문자,숫자 외 제거
    while len(strs)>1:
        if strs.popleft()!=strs.pop(): #list의 pop(0) O(n)이지만 Deque의 popleft()는 O(1)
            return False
    return True

def slicing(s:str)->bool:
    s=s.lower()
    #정규식 이용
    s = typing.sub('[^a-z0-9]','',s)
    return s ==s[::-1] #슬라이싱

TC=int(input())
for test_case in range(1,TC+1):
    s = input()
    #my(s)
    #print(toList(s))
    print(toDeque(s))

# 문자열 처리는 슬라이싱이 가장 빠르다.
'''
s[1:4] 인덱스 1에서 4이전
s[1:} 인덱스 1부터 끝까지
s[:] 문자열 사본을 리턴
s[:-3] 뒤에서 3개 글자 앞까지
s[-3:] 뒤에서 3개글자 에서 끝까지
s[::1] 기본값
s[::-1] 뒤집기
s[::2] 2칸씩 띄어서
'''