#jewels_and_stones.py

import sys
sys.stdin = open('input/jewels_and_stones')
import collections

def my(j:str, s:str)->int:
    strCount = collections.Counter(s)
    sum =0
    for i in j:
        sum+=strCount[i]
    return sum

def jewels_and_stones(J:str,S:str)->int:
    freqs = {}
    count = 0
    for char in S:
        if char not in freqs:
            freqs[char]=1
        else :
            freqs[char]+=1

    for char in J:
        if char in freqs:
            count+=freqs[char]
    return count

def using_defaultdict(J:str, S:str)->int:
    freqs = collections.defaultdict(int)
    count = 0

    for char in S :
        freqs[char]+=1
    for char in J:
        count+=freqs[char]
    return count

def using_counter(J:str, S:str)->int:
    freqs = collections.Counter(S)
    count = 0
    for char in J:
        count+=freqs[char]
    return count

def pythonic_way(J:str, S:str)->int:
    return sum(s in J for s in S)

J = input()
S = input()

print(my(J,S))