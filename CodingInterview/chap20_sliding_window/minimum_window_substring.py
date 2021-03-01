#minimum_window_substring.py
import sys
sys.stdin = open('input/minimum_window_substring')
import collections
from typing import List

def my(T:str,  S:str)->str:
    # 중복 문자 해결 안됌 ex) T:AABBCC  result : AABBC  예상답: ABBC
    sList = list(T)
    forward =0
    backward =0
    strs = collections.deque()
    result = S
    for i,v in enumerate(S):
        if forward ==0 and v in sList:
            forward = i
            sList.remove(v)
            strs.append(i)
        elif v in sList:
            sList.remove(v)
            strs.append(i)
            backward = i
        if not sList:
            if len(T[forward:backward+1])<len(result):
                result = S[forward:backward+1]
            sList.append(S[strs.popleft()])
            forward = strs[0]
    return result

def brute_force(t:str, s:str)->str:
    def contains(s_substr_lst:List, t_lst:List):
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else:
                return False
        return True

    if not s or not t:
        return ''

    window_size = len(t)
    for size in range(window_size, len(s)+1):
        for left in range(len(s)-size+1):
            s_substr = s[left:left+size]
            if contains(list(s_substr),list(t)):
                return s_substr
    return ''

def uisng_window(s:str, t:str)->str:
    need = collections.Counter(t)
    missing = len(t)
    left = start = end =0
    #오른쪽 포인터 이동
    for right ,char in enumerate(s,1): #right는 0 이 아닌 1부터 시작
        missing -= need[char]>0 #char이 need에 존재하면 1
        need[char]-=1
        if missing ==0: #필요 문자가 0 일때
            while left < right and need[s[left]]<0:
                need[s[left]]+=1
                left +=1
            if not end or right-left <=end-start:
                start,end = left, right
            need[s[left]]+=1
            missing+=1
            left+=1
    return s[start:end]

def using_counter(s:str, t:str)->str:
    t_count =collections.Counter(t)
    current_count =collections.Counter()

    start = float('-inf')
    end = float('inf')
    left = 0

    for right, char in enumerate(s,1):
        current_count[char]+=1
        #AND 연산 결과로 왼쪽 포인터 이동 판단
        while current_count & t_count==t_count:
            if right-left <end-start:
                start, end = left, right
            current_count[s[left]]-=1
            left+=1
    return s[start:end] if end-start <=len(s) else ''

T = input()
S = input()
#answer = my(T,S)
#answer = brute_force(T,S)
#answer = uisng_window(S,T)
answer = practice(S,T)
print(answer)

