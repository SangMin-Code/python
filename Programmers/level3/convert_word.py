#convert_word.py
#https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3
import sys
sys.stdin=open('input/convert_word')
from typing import List

def my(begin:str, target:str, words:List[str])->int:

    if target not in words:
        return 0
    answer = []
    visited = []

    def DFS(word,n):
        if word == target:
            answer.append(n)
        for i,v in enumerate(word):
            if word[i]!=target[i]:
                new_word = word[:i]+target[i]+word[i+1:]
                if new_word in words and new_word not in visited:
                    if new_word != target:
                        visited.append(new_word)
                    DFS(new_word,n+1)
                else :
                    for j in [x for x in words if x[:i]+x[i+1:] == word[:i]+word[i+1:]]:
                        if j not in visited:
                            if j != target:
                                visited.append(j)
                            DFS(j,n+1)
    DFS(begin,0)
    return min(answer)


TC = int(input())
for test_case in range(1,TC+1):
    begin, target = input().split()
    words = list(input().split())
    answer = my(begin, target, words)
    print(answer)