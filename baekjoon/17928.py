# 17928.py
#stack 스택
import sys
from typing import List

sys.stdin = open('input/17928')
'''
시간 초과  -> O(n**2)  
def my(n:int, sequence:List[int])->List[int]:
    answer = []
    for i,val in enumerate(sequence): #list안의 모든 원소마다
        if i==n-1:                    # sequence[-1] 의 오큰수는 없으므로 항상 -1
            answer.append(-1)
        else :
            for j in range(i+1,n):      # sequence[i+1:]에 대해 오큰수를 확인
                if sequence[j]>val:     # 도중에 오큰수를 만나면 answer에 append 끝까지 못찾으면 -1
                    answer.append(sequence[j])
                    break
                elif sequence[j]<=val and j==n-1:
                    answer.append(-1)
    return answer
'''
def my(n:int, sequence:List[int])->List[int]:
    # 가장 최근이 넣은 값과 진행 값과의 비교하는것을 반복하면 오른쪽에서 첫번째로 자신보다 큰 수를 찾을 수 있다.
    # stack 안에 있는 원소의 크기와 i번째 list와 비교
    # stack[-1]이  seqence[i]보다 작으면 stack을 pop 시키는것을 반복
    # -> 진행하면서 stack[-1]은 항상 sequence[i]보다는 크거나 같은 값만 남아있음.
    # stack을 이용하여 풀이하므로 stack[-1]의 순서가 지켜지지 않으므로
    # stack에 넣을 때 idx를 같이 넣어준다.

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