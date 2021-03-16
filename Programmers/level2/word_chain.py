#word_chain.py
#https://programmers.co.kr/learn/courses/30/lessons/12981
import sys
sys.stdin=open('input/word_chain')
from typing import List

def my(n:int, words:List[str])->List[int]:
    prev_word = ''
    used_words =[]
    for idx,word in enumerate(words):
        if idx!=0:
            if word in used_words or word[0]!=prev_word:
                return [idx%n+1,idx//n +1]
        used_words.append(word)
        prev_word=word[-1]
    return [0,0]

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    words = list(input().split())
    answer = my(n,words)
    print(answer)