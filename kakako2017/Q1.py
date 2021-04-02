#Q1.py
import sys
sys.stdin=open('input/Q1')
from typing import List

def my(n,arr1:List[int],arr2:List[int])->List[str]:
    answer = []
    for i in range(n):
        arr1[i] = (n-len(bin(arr1[i])[2:]))*'0'+bin(arr1[i])[2:]
        arr2[i]= (n-len(bin(arr2[i])[2:]))*'0'+bin(arr2[i])[2:]
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1[i][j]==arr2[i][j]=='0':
                temp+=' '
            else:
                temp+='#'
        answer.append(temp)
    return answer

def solution(n,arr1:List[int],arr2:List[int])->List[str]:
    maps = []
    for i in range(n):
        #or 연산 후 이진수 변환
        maps.append(
            bin(arr1[i]|arr2[i])[2:]
            .zfill(n)
            .replace('1','#')
            .replace('0',' ')
        )
    return maps


TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int, input().split()))
    #answer =my(n,arr1,arr2)
    answer = solution(n, arr1, arr2)
    print(answer)