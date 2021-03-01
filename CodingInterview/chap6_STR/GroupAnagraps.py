#GroupAnagrams.py
import sys
import collections
from typing import List
sys.stdin = open('input/GroupAnagrams','r')

def my(words:List[str])->List[List[str]]:
    pass

def groupAnagrams(strs:List[str])->List[List[str]]:
    anagrams = collections.defaultdict(list)
    for word in strs:
        #정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word) #''.join(list) list를 문자열료 변환
    return anagrams.values()


words = list(input().split())
print(groupAnagrams(words))