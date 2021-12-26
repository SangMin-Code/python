import sys
from typing import List
import itertools
sys.stdin = open('Programmers/level2/input/vowel_dictionary.txt')


def soultion(word: str) -> int:
    vowel = ['1', '2', '3', '4', '5']
    vowel_convert = [['A', '1'], ['E', '2'],
                     ['I', '3'], ['O', '4'], ['U', '5']]
    list = []
    for i in range(1, 6):
        for j in itertools.product(vowel, repeat=i):
            list.append(float('0.'+''.join(j)))
    list.sort()

    for s, n in vowel_convert:
        word = word.replace(s, n)
    word = float('0.'+word)
    return (list.index(word)+1)


TC = int(input())
for i in range(TC):
    word = input()
    result = soultion(word)
    print(result)
