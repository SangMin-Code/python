#just_that_music.py
#https://programmers.co.kr/learn/courses/30/lessons/17683
import sys
sys.stdin=open('input/just_that_music')
from typing import List

def my(m:str, musicinfos:List[str])->str:
    answer = '(None)'
    max_length = 0
    dic = {'C#':'H','D#':'I','F#':'J','G#':'K','A#':'L'}
    for i in dic:
        m=m.replace(i,dic[i])

    for i in musicinfos:
        start, end, title, melody = i.split(',')
        for i in dic:
            melody=melody.replace(i,dic[i])
        s = list(map(int,start.split(":")))
        e = list(map(int,end.split(":")))
        time = (e[0]-s[0])*60 + e[1]-s[1]
        played = ''
        if len(melody)>time:
            played = melody[:time]
        else :
            played = melody*(time//len(melody))+melody[:time%len(melody)]
        if m in played and time >max_length :
            answer = title
            max_length =time
    return answer


TC = int(input())
for test_case in range(1,TC+1):
    m,n = input().split()
    musicinfos = []
    for _ in range(int(n)):
        musicinfos.append(input())
    answer = my(m,musicinfos)
    print(answer)