# 17928.py
#stack 스택
import sys
from typing import List

sys.stdin = open('input/17928')
'''
시간 초과
def my(n:int, sequence:List[int])->List[int]:
    answer = []
    for i,val in enumerate(sequence):
        if i==n-1:
            answer.append(-1)
        else :
            for j in range(i+1,n):
                if sequence[j]>val:
                    answer.append(sequence[j])
                    break
                elif sequence[j]<=val and j==n-1:
                    answer.append(-1)
    return answer
'''
def my(n:int, sequence:List[int])->List[int]:
    answer=[-1]*n
    stack=[]
    for i,val in enumerate(sequence):
        while stack and stack[-1][0]<val:
            answer[stack.pop()[1]]=val
        stack.append([val,i])
    return answer

TC = int(input())
for test_case in range(1, TC + 1):
    n = int(sys.stdin.readline().rstrip())
    sequence = list(map(int,sys.stdin.readline().rstrip().split()))
    answer = my(n,sequence)
    print(' '.join(str(x) for x in answer))