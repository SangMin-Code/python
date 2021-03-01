import sys
sys.stdin = open('input/palindrome_pairs')
from typing import List

#TODO 470P

def my(words:List[str])->List[List[str]]:
    result = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i==j:
                continue
            words = word1+word2
            if words == words[::-1]:
                result.append([i,j])
    return result

def broot_force(words:List[str])->List[List[int]]:
    def is_palindrome(word):
        return word==word[::-1]
    output = []
    for i, word1 in enumerate(words):
        for j, word2 in enumerate(words):
            if i == j:
                continue
            if is_palindrome(word1+word2):
                output.append([i,j])
    return output

TC = int(input())
for test_case in range(TC, TC+1):
    words = list(input().split())
    answer = my(words)
