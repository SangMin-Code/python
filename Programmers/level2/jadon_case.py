#jadon_case.py
#https://programmers.co.kr/learn/courses/30/lessons/12951
import sys
sys.stdin=open('input/jadon_case')
from typing import List

def my(letters : str)->str:
    #문자의 공백 처리가 어려움 - 문자 앞뒤에 공백이 있을 경우
    # 한 문자로 뽑아내어 처리하기 ??
    # .title() 사용시 모든 문자의 첫번째 글자가 대문자 (숫자가 있으면 숫자 다음 문자가 대문자)
    for i in range(1,len(letters)-1):
        if letters[i]==' ' and (letters[i-1]!=' ' and letters[i-1]!='#'):
            letters = letters[:i]+'#'+letters[i+1:]

    words = list(letters.split('#'))
    for i,word in enumerate(words):
        str = word.lower()
        if str[0] is ' ':
            for j in range(len(word)) :
                if word[j]!=' ' and not word[j].isdigit():
                    str = str[:j]+str[j].upper()+str[j+1:]
                    break
        elif not word[0].isdigit():
            str= str[0].upper() + str[1:]
        words[i]=str

    return ' '.join(words)

TC = int(input())
for test_case in range(1,TC+1):
 str = input()
 print(my(str))