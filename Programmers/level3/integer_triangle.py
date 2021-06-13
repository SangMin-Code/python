#integer_triangle.py
import sys
sys.stdin=open('input/integer_triangle')
from typing import List

def my(triangle:List[List[int]])->int:
    answer = 0
    for i,v in enumerate(triangle) :
        if i == 0 :
            continue
        else :
            for j,val in enumerate(v):
                if j == 0 :
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j]
                elif j==len(v)-1:
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j-1]
                else :
                    triangle[i][j]= max(triangle[i][j]+triangle[i-1][j-1],triangle[i][j]+triangle[i-1][j])
    answer = max(triangle[-1])
    return answer

def my2(triangle:List[List[int]])->int:
    answer = 0
    for i,v in enumerate(triangle) :
        if i == 0 :
            continue
        else :
            for j,val in enumerate(v):
                if j == 0 :
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j] #왼쪽
                elif j==len(v)-1:
                    triangle[i][j] = triangle[i][j]+triangle[i-1][j-1] #오른쪽
                else :
                    triangle[i][j]= max(triangle[i][j]+triangle[i-1][j-1],triangle[i][j]+triangle[i-1][j]) #중간부분들
    answer = max(triangle[-1])
    return answer

TC = int(input())
for test_case in range(1,TC+1):
    n = int(input())
    triangle = []
    for _  in range(n):
        triangle.append(list(map(int,input().split())))
    answer = my(triangle)
    print(answer)