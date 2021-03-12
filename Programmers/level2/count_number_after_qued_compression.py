#count_number_after_qued_compression.py
#https://programmers.co.kr/learn/courses/30/lessons/68936
import sys
sys.stdin=open('input/count_number_after_qued_compression')
from typing import List

def my(arr:List[List[int]])->List[int]:
    n = len(arr)
    answer = [0,0]
    def reculsion(point:List[int], n:int):
        if n >0:
            total =0
            for i in range(n):
                total+= sum(arr[point[0]+i][point[1]:point[1]+n])
            if total == 0:
                answer[0]=answer[0]+1
            elif total == n**2:
                answer[1]=answer[1]+1
            else :
                reculsion([point[0],point[1]], n//2)
                reculsion([point[0]+n//2,point[1]], n//2)
                reculsion([point[0]+n//2,point[1]+n//2], n//2)
                reculsion([point[0],point[1]+n//2], n//2)
    reculsion([0,0],n)
    return answer



TC = int(input())
for test_case in range(1,TC+1):
    n=int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int,input().split())))
    answer = my(arr)
    print(answer)