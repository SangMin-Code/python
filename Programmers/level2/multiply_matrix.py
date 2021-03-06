#multiply_matrix.py
#https://programmers.co.kr/learn/courses/30/lessons/12949
import sys
sys.stdin=open('input/multiply_matrix')
from typing import List

def my(arr1:List[List[int]], arr2:List[List[int]])->List[List[int]]:
    answer = [[0]*len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    return answer
#zip 활용법??

TC = int(input())
for test_case in range(1,TC+1):
    arr1,arr2 = [],[]
    n = int(input())
    for n in range(n):
        arr1.append(list(map(int,input().split())))
    n =int(input())
    for n in range(n):
        arr2.append((list(map(int,input().split()))))
    answer =my(arr1,arr2)
    print(answer)