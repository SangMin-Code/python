import sys
sys.stdin = open('input/valid_anagram')

def my(s:str,t:str)->bool:
    return sorted(s)==sorted(t)

def is_anagram(s:str,t:str)->bool:
    return sorted(s)==sorted(t)

TC = int(input())
for test_case in range(1,TC+1):
    s = input()
    t = input()

    my(s,t)